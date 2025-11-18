import vapoursynth as vs
core = vs.core
import havsfunc as haf
import fvsfunc as fvf
import xvs as xvs

src = core.d2v.Source(r'C:\Users\Kids.KIDS-PC\AppData\Local\Programs\RAW\Volume 5\06.d2v')
src = core.vivtc.VFM(src, order=1, cthresh=10)
src = core.vivtc.VDecimate(src)
src = core.std.Crop(src, left=4, right=4, top=4, bottom=4)
src = src if not core.text.FrameProps(src,'_Transfer') else core.std.SetFrameProps(src, _Transfer=5)
src = src if not core.text.FrameProps(src,'_Primaries') else core.std.SetFrameProps(src, _Primaries=5)
src = core.std.SetFrameProp(src, prop="_ColorRange", intval=1)
src = fvf.AutoDeblock(src)
src = haf.EdgeCleaner(src)
src = core.dfttest.DFTTest(src, sigma=1)
src = core.neo_f3kdb.Deband(src)
src = haf.GrainFactory3(src, g1str=3.5, g2str=2.5, g3str=1.5, g1shrp=30, g2shrp=33, g3shrp=40, g1size=0.7, g2size=0.6, g3size=0.45, temp_avg=0, ontop_grain=0.0, seed=-1, th1=12, th2=28, th3=64, th4=80)
src = core.fmtc.resample(src, kernel="Spline36", w=720, h=480, interlaced=False, interlacedd=False)
src = xvs.mwaa(src)
src = core.resize.Spline36(src, format=vs.YUV420P10, range_s="limited")
src.set_output(index=0)