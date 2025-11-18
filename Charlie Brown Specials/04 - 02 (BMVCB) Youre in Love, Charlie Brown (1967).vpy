import vapoursynth as vs
core = vs.core
import havsfunc as haf

src = core.ffms2.Source(r'C:\Users\WIP\AppData\Local\Programs\MPEG\04 - 02 (BMVCB) Youre in Love, Charlie Brown (1967).mkv')
src = core.bifrost.Bifrost(src, interlaced=True)#Rainbowing after telecline
src = core.vivtc.VFM(src, order=1, cthresh=10)
src = core.vivtc.VDecimate(src, chroma=True)
src = core.std.Crop(src, left=6, right=6, top=6, bottom=6)
src = core.resize.Spline36(src, width=640, height=480)
super = core.mv.Super(src, pel=2, sharp=1)
backward_vec2 = core.mv.Analyse(super, isb = True, delta = 2, overlap=4)
backward_vec1 = core.mv.Analyse(super, isb = True, delta = 1, overlap=4)
forward_vec1 = core.mv.Analyse(super, isb = False, delta = 1, overlap=4)
forward_vec2 = core.mv.Analyse(super, isb = False, delta = 2, overlap=4)
video = core.mv.Degrain2(src, super,backward_vec1,forward_vec1,backward_vec2,forward_vec2,thsad=400)#Temporal Degrain
src = haf.santiag(src)#Simple AA. Daa sharpens too much and destroys fine detail.
src = haf.EdgeCleaner(src, rmode=17, smode=1)
src = haf.FineDehalo2(src)
src = core.fft3dfilter.FFT3DFilter(src, sigma=1)
src = core.neo_f3kdb.Deband(src)
src = haf.GrainFactory3(src, g1str=3.5, g2str=2.5, g3str=1.5, g1shrp=30, g2shrp=33, g3shrp=40, g1size=0.7, g2size=0.6, g3size=0.45, temp_avg=0, ontop_grain=0.0, seed=-1, th1=12, th2=28, th3=64, th4=80)
src.set_output(index=0)