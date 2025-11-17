import vapoursynth as vs
core = vs.core
import havsfunc as haf
import hnwvsfunc
import mvsfunc as mvf
import fvsfunc as fvf
import muvsfunc as muf
from acsuite import eztrim

src = core.d2v.Source(r'C:\Users\WiP\AppData\Local\Programs\Disney Gold Disc This is Your Life, Donald Duck JP-LD.d2v')
src = core.bifrost.Bifrost(src, interlaced=True)
src = core.ssiq.SSIQ(src, interlaced=True)
src = core.vivtc.VFM(src, order=1, cthresh=10)
src = core.vivtc.VDecimate(src)
src = core.std.Crop(src, right=12, left=12, bottom=8, top=2)#Put crop after decimating, if not chroma bleeding occurs. Interlaced 4:2:0 has mod4 and mod12 restrictions.
src = core.std.Trim(src, first=620, last=50044)
src = fvf.AutoDeblock(src, edgevalue=24, db1=1, db2=6, db3=15, deblocky=True, deblockuv=True, debug=False, redfix=False, fastdeblock=False, adb1=3, adb2=4, adb3=8, adb1d=2, adb2d=7, adb3d=11, planes=None)
src = haf.santiag(src)
src = haf.STPresso(src)
src = haf.FineDehalo(src, brightstr=1.02)
src = haf.EdgeCleaner(src)
src = haf.FixChromaBleedingMod(src, cx=4, cy=4, thr=4.0, strength=0.8, blur=False)
strength=2
src = core.fft3dfilter.FFT3DFilter(src, bw=6, bh=6, ow=3, oh=3, bt=1,
sigma=strength)
src = core.fft3dfilter.FFT3DFilter(src, bw=216, bh=216, ow=108, oh=108,
bt=1, sigma=strength/8, sigma2=strength/4, sigma3=strength/2, sigma4=strength)#Two-Pass Denoise
src = muf.SmoothGrad(src)
src = muf.GradFun3(src, thr=0.75, radius=12)
src = haf.GrainFactory3(src, g1str=3.5, g2str=2.5, g3str=1.5, g1shrp=30, g2shrp=33, g3shrp=40, g1size=0.7, g2size=0.6, g3size=0.45, temp_avg=0, ontop_grain=0.0, seed=-1, th1=12, th2=28, th3=64, th4=80)
src = core.fmtc.resample(src, kernel="Spline36", w=640, h=480, interlaced=False, interlacedd=False)
src = core.resize.Spline36(src, format=vs.YUV420P10, range_s="limited")
src.set_output(index=0)

