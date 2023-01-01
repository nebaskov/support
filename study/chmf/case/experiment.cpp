#include <cmath>


/**
 * Convert polynomial order in Noll notation into n/m
 * @param p (i) - order of Zernike polynomial in Noll notation
 * @param N (o) - order of polynomial
 * @param M (o) - angular parameter
 */
void convert_Zidx(int p, int *N, int *M){
	int n = (int) floor((-1.+sqrt(1.+8.*p)) / 2.);
	*M = (int)(2.0*(p - n*(n+1.)/2. - 0.5*(double)n));
	*N = n;
}

/**
 * Calculate value of Zernike polynomial on rectangle matrix WxH pixels
 * Center of matrix will be zero point
 * Scale will be set by max(W/2,H/2)
 * @param n - order of polynomial (max: 100!)
 * @param m - angular parameter of polynomial
 * @param W - width of output array
 * @param H - height of output array
 * @param norm (o) - (if !NULL) normalize factor
 * @return NULL-terminated array of Zernike polynomials on given matrix
 */
double *zernfunR(int n, int m, int W, int H, double *norm){
	double Z = 0., *Zarr = NULL;
	bool erparm = false;
	if(W < 2 || H < 2)
		errx(1, "Sizes of matrix must be > 2!");
	if(n > 100)
		errx(1, "Order of Zernike polynomial must be <= 100!");
	if(n < 0) erparm = true;
	if(n < iabs(m)) erparm = true; // |m| must be <= n
	int d = n - m;
	if(d % 2) erparm = true; // n-m must differ by a prod of 2
	if(erparm)
		errx(1, "Wrong parameters of Zernike polynomial (%d, %d)", n, m);
	if(!FK) build_factorial();
	double Xc = (W - 1.) / 2., Yc = (H - 1.) / 2., Rnorm = fmax(Xc, Yc); // coordinate of circle's middle
	int i, j, k, m_abs = iabs(m), iup = (n-m_abs)/2, N = n+1, w = (W+1)/2, h = (H+1)/2, S=w*h;
	double **Rpow = MALLOC(double*, N); // powers of R
	Rpow[0] = MALLOC(double, S);
	for(j = 0; j < S; j++) Rpow[0][j] = 1.; // zero's power
	double *R = MALLOC(double, S);
	// first - fill array of R
	double xstart = (W%2) ? 0. : 0.5, ystart = (H%2) ? 0. : 0.5;
	for(j = 0; j < h; j++){
		double *pt = &R[j*w], x, ww = w;
		for(x = xstart; x < ww; x++, pt++){
			double yy = (j + ystart)/Rnorm, xx = x/Rnorm;
			*pt = sqrt(xx*xx+yy*yy);
		}
	}
	for(i = 1; i < N; i++){ // Rpow - is quater I of cartesian coordinates ('cause other are fully simmetrical)
		Rpow[i] = MALLOC(double, S);
		double *rp = Rpow[i], *rpo = Rpow[i-1];
		for(j = 0; j < h; j++){
			int idx = j*w;
			double *pt = &rp[idx], *pto = &rpo[idx], *r = &R[idx];
			for(k = 0; k < w; k++, pt++, pto++, r++)
				*pt = (*pto) * (*r); // R^{n+1} = R^n * R
		}
	}
	int SS = W * H;
	// now fill output matrix
	Zarr = MALLOC(double, SS); // output matrix W*H pixels
	double ZSum = 0.;
	for(j = 0; j < H; j++){
		double *Zptr = &Zarr[j*W];
		double Ryd = fabs(j - Yc);
		int Ry = w * (int)Ryd; // Y coordinate on R matrix
		for(i = 0; i < W; i++, Zptr++){
			Z = 0.;
			double Rxd = fabs(i - Xc);
			int Ridx = Ry + (int)Rxd; // coordinate on R matrix
			if(R[Ridx] > 1.) continue; // throw out points with R>1
			// calculate R_n^m
			for(k = 0; k <= iup; k++){ // Sum
				double z = (1. - 2. * (k % 2)) * FK[n - k]        //       (-1)^k * (n-k)!
					/(//----------------------------------- -----   -------------------------------
						FK[k]*FK[(n+m_abs)/2-k]*FK[(n-m_abs)/2-k] // k!((n+|m|)/2-k)!((n-|m|)/2-k)!
					);
				Z += z * Rpow[n-2*k][Ridx];  // *R^{n-2k}
			}
			// normalize
			double eps_m = (m) ? 1. : 2.;
			Z *= sqrt((double)(n+1) / M_PI / eps_m);
			double theta = atan2(j - Yc, i - Xc);
			// multiply to angular function:
			if(m){
				if(m > 0)
					Z *= cos(theta*(double)m_abs);
				else
					Z *= sin(theta*(double)m_abs);
			}
			*Zptr = Z;
			ZSum += Z*Z;
		}
	}
	if(norm) *norm = ZSum;
	// free unneeded memory
	FREE(R);
	for(i = 0; i < N; i++) FREE(Rpow[i]);
	FREE(Rpow);
	return Zarr;
}

/**
 * Zernike polynomials in Noll notation for square matrix
 * @param p - index of polynomial
 * @other params are like in zernfunR
 * @return zernfun
 */
double *zernfunNR(int p, int W, int H, double *norm){
	int n, m;
	convert_Zidx(p, &n, &m);
	return zernfunR(n,m,W,H,norm);
}

/**
 * Zernike decomposition of image 'image' WxH pixels
 * @param Nmax (i) - maximum power of Zernike polinomial for decomposition
 * @param W, H (i) - size of image
 * @param image(i) - image itself
 * @param Zsz  (o) - size of Z coefficients array
 * @param lastIdx (o) - (if !NULL) last non-zero coefficient
 * @return array of Zernike coefficients
 */
double *Zdecompose(int Nmax, int W, int H, double *image, int *Zsz, int *lastIdx){
	int i, SS = W*H, pmax, maxIdx = 0;
	double *Zidxs = NULL, *icopy = NULL;
	pmax = (Nmax + 1) * (Nmax + 2) / 2; // max Z number in Noll notation
	printf("pmax = %d\n", pmax);
	Zidxs = MALLOC(double, pmax);
	icopy = MALLOC(double, W*H);
	memcpy(icopy, image, W*H*sizeof(double)); // make image copy to leave it unchanged
	*Zsz = pmax;
	for(i = 0; i < pmax; i++){ // now we fill array
		double norm, *Zcoeff = zernfunNR(i, W, H, &norm);
		int j;
		double *iptr = icopy, *zptr = Zcoeff, K = 0.;
		for(j = 0; j < SS; j++, iptr++, zptr++)
			K += (*zptr) * (*iptr) / norm; // multiply matrixes to get coefficient
		Zidxs[i] = K;
		if(fabs(K) < Z_prec){
			Zidxs[i] = 0.;
			continue; // there's no need to substract values that are less than our precision
		}
		maxIdx = i;
		iptr = icopy; zptr = Zcoeff;
		for(j = 0; j < SS; j++, iptr++, zptr++)
			*iptr -= K * (*zptr); // subtract composed coefficient to reduce high orders values
		FREE(Zcoeff);
	}
	if(lastIdx) *lastIdx = maxIdx;
	FREE(icopy);
	return Zidxs;
}

/**
 * Zernike restoration of image WxH pixels by Zernike polynomials coefficients
 * @param Zsz  (i) - number of elements in coefficients array
 * @param Zidxs(i) - array with Zernike coefficients
 * @param W, H (i) - size of image
 * @return restored image
 */
double *Zcompose(int Zsz, double *Zidxs, int W, int H){
	int i, SS = W*H;
	double *image = MALLOC(double, SS);
	for(i = 0; i < Zsz; i++){ // now we fill array
		double K = Zidxs[i];
		if(fabs(K) < Z_prec) continue;
		double *Zcoeff = zernfunNR(i, W, H, NULL);
		int j;
		double *iptr = image, *zptr = Zcoeff;
		for(j = 0; j < SS; j++, iptr++, zptr++)
			*iptr += K * (*zptr); // add next Zernike polynomial
		FREE(Zcoeff);
	}
	return image;
}