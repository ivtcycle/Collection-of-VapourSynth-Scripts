import vapoursynth as vs
core = vs.core
import havsfunc as haf

src = core.d2v.Source(r'C:\Users\Kids.KIDS-PC\AppData\Local\Programs\Why Charlie Brown, Why.d2v')
src = core.bifrost.Bifrost(src, interlaced=True)
src = core.vivtc.VFM(src, order=1, cthresh=10)
src = core.vivtc.VDecimate(src)
src = core.std.Crop(src, left=12, right=12, top=12, bottom=12)
src = core.resize.Spline36(src, width=640, height=480)
src = core.std.Trim(src, first=71667, last=106083)
super = core.mv.Super(src, pel=2, sharp=1)
backward_vec2 = core.mv.Analyse(super, isb = True, delta = 2, overlap=4)
backward_vec1 = core.mv.Analyse(super, isb = True, delta = 1, overlap=4)
forward_vec1 = core.mv.Analyse(super, isb = False, delta = 1, overlap=4)
forward_vec2 = core.mv.Analyse(super, isb = False, delta = 2, overlap=4)
video = core.mv.Degrain2(src, super,backward_vec1,forward_vec1,backward_vec2,forward_vec2,thsad=400)#Temporal Degrain
src = core.dedot.Dedot(src)
src = haf.Deblock_QED(src, quant1=25, quant2=26, aOff1=1, bOff1=2, aOff2=1, bOff2=2, uv=3)
src = haf.santiag(src)
src = haf.FineDehalo(src)
src = haf.EdgeCleaner(src, smode=17, hot=True)
src =haf.FixChromaBleedingMod(src)
strength=2
src = core.fft3dfilter.FFT3DFilter(src, bw=6, bh=6, ow=3, oh=3, bt=1,
sigma=strength)
src = core.fft3dfilter.FFT3DFilter(src, bw=216, bh=216, ow=108, oh=108,
bt=1, sigma=strength/8, sigma2=strength/4, sigma3=strength/2, sigma4=strength)#Two-Pass Denoise
src = core.neo_f3kdb.Deband(src)
src = haf.GrainFactory3(src, g1str=3.5, g2str=2.5, g3str=1.5, g1shrp=30, g2shrp=33, g3shrp=40, g1size=0.7, g2size=0.6, g3size=0.45, temp_avg=0, ontop_grain=0.0, seed=-1, th1=12, th2=28, th3=64, th4=80)
src = core.resize.Spline36(src, format=vs.YUV420P10, range_s="limited")
src.set_output(index=0)