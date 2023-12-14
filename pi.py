import time as tm;import mpmath as mp;s=tm.time();mp.mp.dps=314;
a,b=mp.mpf(1),mp.fdiv(1,mp.sqrt(2));d=mp.mpf(.25);p=lambda n:mp.nprint(a*a/d,n)#
for n in range(8):x=(mp.fdiv(a+b,2),mp.sqrt(a*b));y=x[0]-a;d-=y**2*2**n;a,b=x  #
p(314);t=lambda:print(f" in {(tm.time()-s)*1000.0:.1f}ms.");t()