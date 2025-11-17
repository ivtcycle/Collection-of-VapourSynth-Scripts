import vapoursynth as vs
core = vs.core
import havsfunc as haf

src = core.ffms2.Source(r'C:\Users\WIP\AppData\Local\Programs\MPEG Video\02 - 01 (Snow Days) Shes a Good Skate, Charlie Brown (1980).mkv')
src = core.std.Crop(src, left=4, right=4, top=2, bottom=2)
src = core.resize.Spline36(src, width=640, height=480)
src = haf.daa(src)##AA+contra-sharpening
super = core.mv.Super(src, pel=2, sharp=1)
backward_vec2 = core.mv.Analyse(super, isb = True, delta = 2, overlap=4)
backward_vec1 = core.mv.Analyse(super, isb = True, delta = 1, overlap=4)
forward_vec1 = core.mv.Analyse(super, isb = False, delta = 1, overlap=4)
forward_vec2 = core.mv.Analyse(super, isb = False, delta = 2, overlap=4)
video = core.mv.Degrain2(src, super,backward_vec1,forward_vec1,backward_vec2,forward_vec2,thsad=400)#Temporal Degrain
src = core.deblock.Deblock(src, quant=30) 
strength=2
src = core.fft3dfilter.FFT3DFilter(src, bw=6, bh=6, ow=3, oh=3, bt=1,
sigma=strength)
src = core.fft3dfilter.FFT3DFilter(src, bw=216, bh=216, ow=108, oh=108,
bt=1, sigma=strength/8, sigma2=strength/4, sigma3=strength/2, sigma4=strength)#Two-Pass Denoise
src = core.neo_f3kdb.Deband(src)
src = core.grain.Add(src, var=2, seed=-1)
src = core.resize.Spline36(src, format=vs.YUV420P10, range_s="limited")
src.set_output(index=0)