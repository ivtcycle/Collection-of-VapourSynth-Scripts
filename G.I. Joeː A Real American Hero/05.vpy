import vapoursynth as vs
core = vs.core
import havsfunc as haf
import hnwvsfunc
import mvsfunc as mvf
import fvsfunc as fvf
import xvs as xvs

src = core.d2v.Source(r'C:\Users\WIP\AppData\Local\Programs\G.I. Joe Part 1\GI_JOE_1\VIDEO_TS\VTS_05_1.d2v')+ core.d2v.Source(r'C:\Users\WIP\AppData\Local\Programs\G.I. Joe Part 1\GI_JOE_1\VIDEO_TS\VTS_05_2.d2v')
src = core.bifrost.Bifrost(src, interlaced=True)
src = core.vivtc.VFM(src, order=1, cthresh=10)
src = core.vivtc.VDecimate(src)
src = core.std.Crop(src, right=6, left=6, bottom=2, top=2)#Put crop after decimating, if not chroma bleeding occurs. Interlaced 4:2:0 has mod4 and mod12 restrictions.
src = fvf.AutoDeblock(src, edgevalue=24, db1=1, db2=6, db3=15, deblocky=True, deblockuv=True, debug=False, redfix=False, fastdeblock=False, adb1=3, adb2=4, adb3=8, adb1d=2, adb2d=7, adb3d=11, planes=None)
src = haf.STPresso(src)
src = haf.FineDehalo(src, brightstr=1.02)
src = haf.EdgeCleaner(src)
src = haf.Vinverse(src)
src = core.dfttest.DFTTest(src, sigma=8)
src =core.neo_f3kdb.Deband(src)
src = haf.GrainFactory3(src, g1str=3.5, g2str=2.5, g3str=1.5, g1shrp=30, g2shrp=33, g3shrp=40, g1size=0.7, g2size=0.6, g3size=0.45, temp_avg=0, ontop_grain=0.0, seed=-1, th1=12, th2=28, th3=64, th4=80)
src = core.fmtc.resample(src, kernel="Spline36", w=640, h=480, interlaced=False, interlacedd=False)
src = xvs.mwaa(src)
src = core.resize.Spline36(src, format=vs.YUV420P10, range_s="limited")
src.set_output(index=0)

#Notes: For interlaced content, do not change the colormatrix unless you are upscaling the dvd. Let x265 choose its limitations. 
