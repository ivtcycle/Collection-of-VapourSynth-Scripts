import vapoursynth as vs
core = vs.core
import havsfunc as haf

src = core.ffms2.Source(r'C:\Users\WIP\AppData\Local\Programs\MPEG Video\02 - 05 (1970s V1) Its a Mystery, Charlie Brown (1974).mkv')
src = core.vivtc.VFM(src, order=1, cthresh=10)
src = core.vivtc.VDecimate(src, chroma=True)
src = core.std.Crop(src, left=4, right=4, top=2, bottom=2)
src = core.resize.Spline36(src, width=640, height=480)
super = core.mv.Super(src, pel=2, sharp=1)
backward_vec2 = core.mv.Analyse(super, isb = True, delta = 2, overlap=4)
backward_vec1 = core.mv.Analyse(super, isb = True, delta = 1, overlap=4)
forward_vec1 = core.mv.Analyse(super, isb = False, delta = 1, overlap=4)
forward_vec2 = core.mv.Analyse(super, isb = False, delta = 2, overlap=4)
video = core.mv.Degrain2(src, super,backward_vec1,forward_vec1,backward_vec2,forward_vec2,thsad=400)#Temporal Degrain
src = haf.daa(src)##AA+contra-sharpening
src = core.fft3dfilter.FFT3DFilter(src,sigma=1.5)
src = core.placebo.Deband(src, grain=2, iterations=2)
src = core.grain.Add(src, var=0.5)
src = core.resize.Spline36(src, format=vs.YUV420P10, range_s="limited")
src.set_output(index=0)