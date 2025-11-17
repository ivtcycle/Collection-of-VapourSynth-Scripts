import vapoursynth as vs
core = vs.core
import havsfunc as haf
import hnwvsfunc
import mvsfunc as mvf
import fvsfunc as fvf

src = core.ffms2.Source(r'C:\Users\WIP\Downloads\Carebears - The Nutcracker.mkv')
src = core.std.AssumeFPS(src, fpsnum=30000, fpsden=1001)
src = core.std.Crop(src, left=4, right=4, top=2, bottom=2)
src = core.vivtc.VFM(src, order=1, cthresh=10)
src = core.vivtc.VDecimate(src)
src = fvf.AutoDeblock(src, edgevalue=24, db1=1, db2=6, db3=15, deblocky=True, deblockuv=True, debug=False, redfix=False, fastdeblock=False, adb1=3, adb2=4, adb3=8, adb1d=2, adb2d=7, adb3d=11, planes=None)
src = haf.santiag(src, pscrn=2)
src = core.ssiq.SSIQ(src, interlaced=0)
src = haf.STPresso(src)
src = haf.EdgeCleaner(src)
src = haf.FineDehalo(src, brightstr=1.02)
src = haf.FixChromaBleedingMod(src)
src = haf.Vinverse(src)
super = core.mv.Super(src, pel=2, sharp=1)
backward_vec2 = core.mv.Analyse(super, isb = True, delta = 2, overlap=4)
backward_vec1 = core.mv.Analyse(super, isb = True, delta = 1, overlap=4)
forward_vec1 = core.mv.Analyse(super, isb = False, delta = 1, overlap=4)
forward_vec2 = core.mv.Analyse(super, isb = False, delta = 2, overlap=4)
video = core.mv.Degrain2(src, super,backward_vec1,forward_vec1,backward_vec2,forward_vec2,thsad=400)
src = core.dfttest.DFTTest(src, sigma=1)
src =core.neo_f3kdb.Deband(src)
src = haf.GrainFactory3(src, g1str=3.5, g2str=2.5, g3str=1.5, g1shrp=30, g2shrp=33, g3shrp=40, g1size=0.7, g2size=0.6, g3size=0.45, temp_avg=0, ontop_grain=0.0, seed=-1, th1=12, th2=28, th3=64, th4=80)
src = core.fmtc.resample(src, kernel="Spline36", w=640, h=480, interlaced=False, interlacedd=False)
src = core.resize.Spline36(src, format=vs.YUV420P10, range_s="limited")
src.set_output(index=0)