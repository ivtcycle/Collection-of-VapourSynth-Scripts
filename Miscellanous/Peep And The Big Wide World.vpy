import vapoursynth as vs
core = vs.core
import havsfunc as haf

src = core.d2v.Source(r'C:\Users\WIP\Downloads\VTS_01_1.d2v')+core.d2v.Source(r'C:\Users\WIP\Downloads\VTS_01_2.d2v')+core.d2v.Source(r'C:\Users\WIP\Downloads\VTS_01_3.d2v')+core.d2v.Source(r'C:\Users\WIP\Downloads\VTS_01_4.d2v')
src = core.vivtc.VFM(src, order=1, cthresh=10)
src = core.vivtc.VDecimate(src)
src = core.std.Crop(src, left=12, right=12, top=12, bottom=12)
src = core.resize.Bicubic(src, width=640, height=480)
src = haf.santiag(src)
src = core.dedot.Dedot(clip, luma_2d, luma_t, chroma_t1, chroma_t2)
src = haf.FineDehalo(src, rx=2, ry=2, thmi=80, thma=128, thlimi=50, thlima=100, darkstr=1, brightstr=1, excl=True, showmask=False)
src = core.fft3dfilter.FFT3DFilter(src, sigma=1)
src = core.neo_f3kdb.Deband(src)
src.set_output(index=0)

'''
Was going to add grain, but the animation is way too flat. The grain stands out like a sore thumb, and becomes dancing grain. Even with a value of 0.1. 
No, I haven't lost my marbles yet. It really is that FLAT. All the filtering is very simple, so skipping grain suprisingly does nothing. 
'''