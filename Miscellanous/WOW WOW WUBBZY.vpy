import vapoursynth as vs
core = vs.core
import havsfunc as haf

src = core.d2v.Source(r'C:\Users\WIP\AppData\Local\Programs\MPEG\WOW WOW WUBBZY\VTS_01_1.d2v')+core.d2v.Source(r'C:\Users\WIP\AppData\Local\Programs\MPEG\WOW WOW WUBBZY\VTS_01_2.d2v')+core.d2v.Source(r'C:\Users\WIP\AppData\Local\Programs\MPEG\WOW WOW WUBBZY\VTS_01_3.d2v')+core.d2v.Source(r'C:\Users\WIP\AppData\Local\Programs\MPEG\WOW WOW WUBBZY\VTS_01_4.d2v')+core.d2v.Source(r'C:\Users\WIP\AppData\Local\Programs\MPEG\WOW WOW WUBBZY\VTS_01_5.d2v')
src = core.vivtc.VFM(src, order=1, cthresh=10)
src = core.vivtc.VDecimate(src, chroma=True)
src = core.std.Crop(src, left=4 , right=4, top=2, bottom=2)
src = core.resize.Spline36(src, width=640, height=480)
src = haf.santiag(src)
src = haf.EdgeCleaner(src, strength=10, rmode=17, smode=1)
src = haf.FineDehalo(src, rx=2, ry=2, thmi=80, thma=128, thlimi=50, thlima=100, darkstr=1, brightstr=1, excl=True, showmask=False)#Very decent picture, but halo heaven.
src = core.fft3dfilter.FFT3DFilter(src, sigma=1)
src = core.neo_f3kdb.Deband(src)
src = haf.GrainFactory3(src, g1str=3.5, g2str=2.5, g3str=1.5, g1shrp=30, g2shrp=33, g3shrp=40, g1size=0.7, g2size=0.6, g3size=0.45, temp_avg=0, ontop_grain=0.0, seed=-1, th1=12, th2=28, th3=64, th4=80)
src = core.resize.Spline36(src, format=vs.YUV420P10, range_s="limited")
src.set_output(index=0)
