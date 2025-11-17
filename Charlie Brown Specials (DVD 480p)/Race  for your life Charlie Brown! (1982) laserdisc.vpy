import vapoursynth as vs
core = vs.core
import havsfunc as haf

#The WORST laserdisc I've ever seen. Thankfully all problems can be fixed with some strong filtering.
src = core.d2v.Source(r'C:\Users\WIP\AppData\Local\Programs\MPEG\Race  for your life Charlie Brown! (1982) laserdisc.d2v')
src = core.bifrost.Bifrost(src, luma_thresh=10.0, variation=15, conservative_mask=False, interlaced=True, blockx=4, blocky=4)
src = core.vivtc.VFM(src, order=1, cthresh=10)
src = core.vivtc.VDecimate(src)
src = core.std.Crop(src, left=16, right=16, top=16, bottom=16)
src = core.resize.Spline36(src, width=640, height=480)
src = core.std.Trim(src, first=1758, last=111359)
super = core.mv.Super(src, pel=2, sharp=1)
backward_vec2 = core.mv.Analyse(super, isb = True, delta = 2, overlap=4)
backward_vec1 = core.mv.Analyse(super, isb = True, delta = 1, overlap=4)
forward_vec1 = core.mv.Analyse(super, isb = False, delta = 1, overlap=4)
forward_vec2 = core.mv.Analyse(super, isb = False, delta = 2, overlap=4)
video = core.mv.Degrain2(src, super,backward_vec1,forward_vec1,backward_vec2,forward_vec2,thsad=400)#Temporal Degrain
src = haf.STPresso(src, limit=3, bias=24, RGmode=4, tthr=12, tlimit=3, tbias=49, back=1)# Dampen the grain just a little, to keep the original look.
src = core.dedot.Dedot(src)
src = haf.Deblock_QED(src, quant1=24, quant2=26, aOff1=1, bOff1=2, aOff2=1, bOff2=2, uv=3)
src = haf.santiag(src)
src = haf.FineDehalo(src)
src = haf.EdgeCleaner(src)
src = haf.FixChromaBleedingMod(src, cx=4, cy=4, thr=4.0, strength=0.8, blur=False)
strength=2
src = core.fft3dfilter.FFT3DFilter(src, bw=6, bh=6, ow=3, oh=3, bt=1,
sigma=strength)
src = core.fft3dfilter.FFT3DFilter(src, bw=216, bh=216, ow=108, oh=108,
bt=1, sigma=strength/8, sigma2=strength/4, sigma3=strength/2, sigma4=strength)#Two-Pass Denoise
#src = core.dfttest.DFTTest(src, sigma=1.5)
src = core.placebo.Deband(src, iterations=2, grain=2)
src = haf.GrainFactory3(src, g1str=3.5, g2str=2.5, g3str=1.5, g1shrp=30, g2shrp=33, g3shrp=40, g1size=0.7, g2size=0.6, g3size=0.45, temp_avg=0, ontop_grain=0.0, seed=-1, th1=12, th2=28, th3=64, th4=80)
src = core.resize.Spline36(src, format=vs.YUV420P10, range_s="limited")
src.set_output(index=0)