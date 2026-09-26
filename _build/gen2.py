import os, html
ROOT='/home/claude/site'
PDF='https://f9dbab49-ed05-4f20-ac02-bf4abc8728ee.filesusr.com/ugd/10d882_'
LOCAL = {
    '177e028357684a59a2d33a03285a786b': 'ww/177e028357684a59a2d33a03285a786b.webp',
    '856e391ecc4e450d9460698c093141b9': 'ww/856e391ecc4e450d9460698c093141b9.webp',
    '588e4bf9325f4fb285ebdfab22f73437': 'ww/588e4bf9325f4fb285ebdfab22f73437.webp',
    'ce964329b2874f80b72edfd8d9dcc4d9': 'ww/ce964329b2874f80b72edfd8d9dcc4d9.webp',
    '5710b969bef94e5792db79cfebe7af3a': 'ww/5710b969bef94e5792db79cfebe7af3a.webp',
    '51e77537ca2f4c648886955bf24ad704': 'ww/51e77537ca2f4c648886955bf24ad704.webp',
    'a9948c1a244b495a9ef32b254769d073': 'ww/a9948c1a244b495a9ef32b254769d073.webp',
    '744e224cf0ed46debc5721f59a2f42fc': 'ww/744e224cf0ed46debc5721f59a2f42fc.webp',
    '40197e43fb6a4f8f9f9134e8b71c6bd3': 'ww/40197e43fb6a4f8f9f9134e8b71c6bd3.webp',
    '4fd2f6aba5c74a99a0fc0cc81238d413': 'ww/4fd2f6aba5c74a99a0fc0cc81238d413.webp',
    'c40251ea7579428bb92d9687e5873bb4': 'ww/c40251ea7579428bb92d9687e5873bb4.webp',
    '4de7dcc3a37f463786779f435e3976c8': 'ww/4de7dcc3a37f463786779f435e3976c8.webp',
    'e55fa2153e2f4ed3ad35e5f74ea6931f': 'ww/e55fa2153e2f4ed3ad35e5f74ea6931f.webp',
    '72d2876967074dddb6c2288d151a3d80': 'ww/72d2876967074dddb6c2288d151a3d80.webp',
    'c70f6595048f4105bcdeb693b390ea63': 'ww/c70f6595048f4105bcdeb693b390ea63.webp',
    'cc50744aa8d045968aea19249d13dfc0': 'ww/cc50744aa8d045968aea19249d13dfc0.webp',
    'b833464237f74ef3a2f6c9039542aea7': 'ps4/b833464237f74ef3a2f6c9039542aea7.webp',
    '55a42e28dfe84288b787115019d4224f': 'ps4/55a42e28dfe84288b787115019d4224f.webp',
    '7607658ee5194926a2f4e1c18f8b03d6': 'ps4/7607658ee5194926a2f4e1c18f8b03d6.webp',
    'ddff0ee936b840b58b4e17070e86bb99': 'ps4/ddff0ee936b840b58b4e17070e86bb99.webp',
    '93c88523bdf34f4cb63766b77dffd8ed': 'ps4/93c88523bdf34f4cb63766b77dffd8ed.webp',
    '69192538e3334ecfa486fc79dbe2a75a': 'ps4/69192538e3334ecfa486fc79dbe2a75a.webp',
    '60f1a7fbbf974df1892600f4909eac17': 'ps4/60f1a7fbbf974df1892600f4909eac17.webp',
    'f01cb47383814bd59799c06a5e1d4696': 'ps4/f01cb47383814bd59799c06a5e1d4696.webp',
    '789629b0696e41bb8c0323ccf29a1329': 'ps4/789629b0696e41bb8c0323ccf29a1329.webp',
    '61f67611447b46dfa3bf42095a0194ac': 'ps4/61f67611447b46dfa3bf42095a0194ac.webp',
    '88270d5e5afe4c9eac00011599b5f310': 'ps4/88270d5e5afe4c9eac00011599b5f310.webp',
    '9070b65765054e5b802f943528a8dd4e': 'arm/9070b65765054e5b802f943528a8dd4e.webp',
    '7c0c63ebe68840488ef60eb6a90c31c2': 'arm/7c0c63ebe68840488ef60eb6a90c31c2.webp',
    '93f1e5d63160463a9512a4e6256e3afc': 'arm/93f1e5d63160463a9512a4e6256e3afc.webp',
    'd0ee1c55507148aa9625c8f713aab0e2': 'arm/d0ee1c55507148aa9625c8f713aab0e2.webp',
    '4a46e8fccf054e509e14bccdc038667c': 'arm/4a46e8fccf054e509e14bccdc038667c.webp',
    'f5dc07ffd83044898d8d9670c5ae8988': 'arm/f5dc07ffd83044898d8d9670c5ae8988.webp',
    'handle-side': 'arm/handle-side.webp',
    'handle-top': 'arm/handle-top.webp',
    'base-front': 'arm/base-front.webp',
    '365baf82cdf848f0b253d0cfa673cab6': 'surf/365baf82cdf848f0b253d0cfa673cab6.webp',
    '887bbeea009a4d7e9f1a9e967962f82e': 'surf/887bbeea009a4d7e9f1a9e967962f82e.webp',
    '1a1bd720d5224772b0e80073c878ec97': 'surf/1a1bd720d5224772b0e80073c878ec97.webp',
    'cdedd622541d4e52abb3d8658d58a25c': 'surf/cdedd622541d4e52abb3d8658d58a25c.webp',
    '0acfd66709bd4873b00e20c52cebfdf7': 'surf/0acfd66709bd4873b00e20c52cebfdf7.webp',
    'c56c15685b884a97bd213ad5c5bce7df': 'surf/c56c15685b884a97bd213ad5c5bce7df.webp',
    'sketch4': 'surf/sketch4.webp',
    'sketch5': 'surf/sketch5.webp',
    '89124fa8255b432cbb1379733fe1a6d9': 'arch/89124fa8255b432cbb1379733fe1a6d9.webp',
    '372ee243775344b987982f11591fe113': 'arch/372ee243775344b987982f11591fe113.webp',
    '13da2d83d3184379817cc9c41ce00761': 'arch/13da2d83d3184379817cc9c41ce00761.webp',
    'db6df9794b70468387337bac4b136805': 'arch/db6df9794b70468387337bac4b136805.webp',
    '7b2d6afc52c34dd1af60969d4ae08728': 'arch/7b2d6afc52c34dd1af60969d4ae08728.webp',
    'e3f8bff0fbde4897a1fefaebf0ed4706': 'arch/e3f8bff0fbde4897a1fefaebf0ed4706.webp',
    '0468515a088c4a458b6315d6b2aa94e0': 'arch/0468515a088c4a458b6315d6b2aa94e0.webp',
    '9df7c971b7a44758b01bf02480a353ee': 'arch/9df7c971b7a44758b01bf02480a353ee.webp',
    '4157e4608e4743b89486fc2807bdd576': 'arch/4157e4608e4743b89486fc2807bdd576.webp',
    '2e6f6634d8b740859e9274eeb40e1200': 'arch/2e6f6634d8b740859e9274eeb40e1200.webp',
    'd096c0bd26794eb9b84eebc7b6eecd24': 'arch/d096c0bd26794eb9b84eebc7b6eecd24.webp',
    'bb4b603af5164f9cb784e0b7f541563a': 'arch/bb4b603af5164f9cb784e0b7f541563a.webp',
    '94879fede5bd41caa6d8b958e77995b8': 'arch/94879fede5bd41caa6d8b958e77995b8.webp',
    '5682c17f011f4dc996adca54a0a730e4': 'arch/5682c17f011f4dc996adca54a0a730e4.webp',
    'dc0ee5ba92314f8fbc6f9f20dab64aa5': 'arch/dc0ee5ba92314f8fbc6f9f20dab64aa5.webp',
    'f6a9caff1c234fa990585501cba2444d': 'arch/f6a9caff1c234fa990585501cba2444d.webp',
    'efee5c7dc3624009950a98a10db5ac8a': 'arch/efee5c7dc3624009950a98a10db5ac8a.webp',
    'c3e561411f1b44d98027a9bf04cebf04': 'arch/c3e561411f1b44d98027a9bf04cebf04.webp',
    'b02269c5b4a1431f9f9ed4fc3e21e849': 'arch/b02269c5b4a1431f9f9ed4fc3e21e849.webp',
    '05bc342935a043a6a19db6a01e401dd6': 'arch/05bc342935a043a6a19db6a01e401dd6.webp',
    'aca41a74e47844df9a6a6834237062e3': 'arch/aca41a74e47844df9a6a6834237062e3.webp',
    'sk-plants': 'arch/sk-plants.webp',
    '5b596562019c4c0b93f3bff4440836f5': 'ind/5b596562019c4c0b93f3bff4440836f5.webp',
    'e879d716f0104552980109b5d38f7e17': 'ind/e879d716f0104552980109b5d38f7e17.webp',
    '62f34abc7b4d41eab9c014c2eeed8b3e': 'ind/62f34abc7b4d41eab9c014c2eeed8b3e.webp',
    '832f0b41f4814688b6242cce7e6beb83': 'ind/832f0b41f4814688b6242cce7e6beb83.webp',
    '4cc53e96dfb44eca9848c0df3b7a80ad': 'ind/4cc53e96dfb44eca9848c0df3b7a80ad.webp',
    '0a8cbc17a8fe46028c9c5177f0108263': 'ind/0a8cbc17a8fe46028c9c5177f0108263.webp',
    '529b31ac137247ec8adafd941f01922a': 'ind/529b31ac137247ec8adafd941f01922a.webp',
    'ddc8bab626d34540a091a131a1eefd80': 'ind/ddc8bab626d34540a091a131a1eefd80.webp',
    '16dbbcd326b84071ad3a918296419b7a': 'ind/16dbbcd326b84071ad3a918296419b7a.webp',
    '5f758b985f8647dc931defb88980907d': 'ind/5f758b985f8647dc931defb88980907d.webp',
    '4b87d34981d641b091da4841201571c3': 'ind/4b87d34981d641b091da4841201571c3.webp',
    '305992c11aee49e988087acdbeaf04e1': 'ind/305992c11aee49e988087acdbeaf04e1.webp',
    '1634382e2ec54ab58a172de0e18880d9': 'ind/1634382e2ec54ab58a172de0e18880d9.webp',
    'fadd4dc943a14846b4ebaa970691121b': 'ind/fadd4dc943a14846b4ebaa970691121b.webp',
    '610633e8242d41318445a973b7727ccd': 'ind/610633e8242d41318445a973b7727ccd.webp',
    '228923a3712c4297a26c0d6f218e73dc': 'ind/228923a3712c4297a26c0d6f218e73dc.webp',
    '33a5678309c2435089c070c8ed387133': 'ind/33a5678309c2435089c070c8ed387133.webp',
    '5543586c803d4db0a51ca48d68b22689': 'ind/5543586c803d4db0a51ca48d68b22689.webp',
    '708d7574b874478b9311446f6da43147': 'ind/708d7574b874478b9311446f6da43147.webp',
    '9ccc6ed6757142a7a38c5e19d8fc8d0e': 'ind/9ccc6ed6757142a7a38c5e19d8fc8d0e.webp',
    'a2c0a98e01e941d9862bf4da6466e25a': 'ind/a2c0a98e01e941d9862bf4da6466e25a.webp',
    'be4ca461c7024f179e70504130eebafd': 'ind/be4ca461c7024f179e70504130eebafd.webp',
    '56da038cba2f409fbb55e24501b887fe': 'ind/56da038cba2f409fbb55e24501b887fe.webp',
    '6b2ec448b7ed4f0db88ed52b4896d951': 'ind/6b2ec448b7ed4f0db88ed52b4896d951.webp',
    'b691b56b4e6a42c2a111f961289ba0af': 'ind/b691b56b4e6a42c2a111f961289ba0af.webp',
    '0acc042adc0748aa968522c0fe840ebe': 'ind/0acc042adc0748aa968522c0fe840ebe.webp',
    '04c60f8435864d50afff8501a1c27955': 'ind/04c60f8435864d50afff8501a1c27955.webp',
    'dce61b286ff6416bb86009251c5df272': 'ind/dce61b286ff6416bb86009251c5df272.webp',
    'eb8bb14948ec41f7ac37c87714ecc91e': 'ind/eb8bb14948ec41f7ac37c87714ecc91e.webp',
    '798392b72e59419e8bd454b9a98931ff': 'ind/798392b72e59419e8bd454b9a98931ff.webp',
    'feb23c9f7e1243e38c863f7e4a2319d1': 'ind/feb23c9f7e1243e38c863f7e4a2319d1.webp',
    '7682c35f544146a499497c21b45d9b44': 'ind/7682c35f544146a499497c21b45d9b44.webp',
    '7ab0b98781e042fa9198a71c3580a1aa': 'ind/7ab0b98781e042fa9198a71c3580a1aa.webp',
    '54e4ba63cc074ca3944589c520d9e862': 'ind/54e4ba63cc074ca3944589c520d9e862.webp',
    '857f6de3009e429cbe6025631c6b3c25': 'ind/857f6de3009e429cbe6025631c6b3c25.webp',
    '87f6050ffd654fd4aa511a5099a3a816': 'ind/87f6050ffd654fd4aa511a5099a3a816.webp',
    '1275e535f0994826969cd0a3b9a7a9b5': 'ind/1275e535f0994826969cd0a3b9a7a9b5.webp',
    '41a3f70764b34b3b937db0ab36309a39': 'ind/41a3f70764b34b3b937db0ab36309a39.webp',
    'abdc11835fec42ada88de5a4a5e7174e': 'ind/abdc11835fec42ada88de5a4a5e7174e.webp',
    'b83480aa903c4ce98bf529a64161bab2': 'ind/b83480aa903c4ce98bf529a64161bab2.webp',
    '954be03392e74d3ba660ca0f9a2f7414': 'ind/954be03392e74d3ba660ca0f9a2f7414.webp',
    '3d5cb70fd3604e8ba93c57c3cbb899dd': 'ind/3d5cb70fd3604e8ba93c57c3cbb899dd.webp',
    '62ef8429d84c4d729b220f38bab43a8f': 'ind/62ef8429d84c4d729b220f38bab43a8f.webp',
    '0b854f5c84a046d3a8a7eecdd1f796b9': 'ind/0b854f5c84a046d3a8a7eecdd1f796b9.webp',
    '0c4735e2e1d54362b619abcd9402b3d9': 'ind/0c4735e2e1d54362b619abcd9402b3d9.webp',
    'ef40b761fcbe4bf0933e0f7e54ced716': 'ind/ef40b761fcbe4bf0933e0f7e54ced716.webp',
    '78c3f1de06ff43dfa07c917f4e1c3fe0': 'ind/78c3f1de06ff43dfa07c917f4e1c3fe0.webp',
    '581fd097a8ba4f54b2094f86a9d2f058': 'ind/581fd097a8ba4f54b2094f86a9d2f058.webp',
    '14f0fcd3956c45a78905e03adec15c14': 'ind/14f0fcd3956c45a78905e03adec15c14.webp',
    '1013ce9be9e0428e9794238032cce509': 'ind/1013ce9be9e0428e9794238032cce509.webp',
    '4b5c4be378d7488dbc7f469d905947d6': 'ind/4b5c4be378d7488dbc7f469d905947d6.webp',
    '01c866ac73c142879b39aa2e19df7c46': 'ind/01c866ac73c142879b39aa2e19df7c46.webp',
    'bc4dae38e23242cba92472108691fc91': 'ind/bc4dae38e23242cba92472108691fc91.webp',
    'db5feb337be948479674554439cee40a': 'ind/db5feb337be948479674554439cee40a.webp',
    '71a2c13349644c80b1607c1e91142022': 'ind/71a2c13349644c80b1607c1e91142022.webp',
    'cf8336bd075447ea85d6ff09f5d1bf2e': 'ind/cf8336bd075447ea85d6ff09f5d1bf2e.webp',
    '2259ad2728594063a88cc991fcc44d33': 'ind/2259ad2728594063a88cc991fcc44d33.webp',
    'c627115361cc45ae918ee18185f2b0fc': 'ind/c627115361cc45ae918ee18185f2b0fc.webp',
    '5ff50d7ee9c04516b51698b600b40d2a': 'ind/5ff50d7ee9c04516b51698b600b40d2a.webp',
    'b24a68b2451e467bb42e59abcf0c5d1f': 'ind/b24a68b2451e467bb42e59abcf0c5d1f.webp',
}
def W(f, w=1200, crop=None):
    i,ext=f.split('.')
    if i in LOCAL:
        return '../assets/img/' + LOCAL[i]
    raise SystemExit(f'Image {f} has no local file in LOCAL (assets/img/). Add it before building.')
def fig(url, alt, cls='', cap=''):
    c=f'<figcaption class="mono-label">{cap}</figcaption>' if cap else ''
    return f'<figure class="{cls}"><img src="{url}" alt="{html.escape(alt)}" loading="lazy">{c}</figure>'
def bento(files, cls, alt, w=1400):
    return f'<div class="bento {cls}">'+''.join(fig(W(f,w),alt) for f in files.split())+'</div>'
def strip(files, alt, label='Process'):
    fl=files.split()
    return (f'<div class="strip-wrap"><div class="strip-bar"><span class="mono-label">{label}</span><span class="strip-ctrl"><span class="strip-count">1 / {len(fl)}</span>'
            '<button type="button" class="sbtn" data-dir="-1" aria-label="Previous">&larr;</button><button type="button" class="sbtn" data-dir="1" aria-label="Next">&rarr;</button></span></div>'
            '<div class="strip" tabindex="0">'+''.join(fig(W(f,1000),alt) for f in fl)+'</div></div>')
def split(text, media, flip=False, cls=''):
    return f'<div class="split{" flip" if flip else ""} {cls}"><div class="split-text">{text}</div><div class="split-media">{media}</div></div>'
def video(yt, title):
    return f'<a class="yt" href="https://www.youtube.com/watch?v={yt}" target="_blank" rel="noopener" data-yt="{yt}" aria-label="Play {html.escape(title)}"><img src="https://i.ytimg.com/vi/{yt}/hqdefault.jpg" alt="" loading="lazy"><span class="yt-play" aria-hidden="true"></span><span class="yt-label mono-label">Play video</span></a>'
def imgs(files, cols=None, alt='', extra=''):
    c=(f' cols-{cols}' if cols else '')+(f' {extra}' if extra else '')
    return f'<div class="pgrid{c}">'+''.join(f'<figure><img src="{W(f)}" alt="{html.escape(alt)}" loading="lazy"></figure>' for f in files.split())+'</div>'
def sec(label, title, body):
    return f'''<section class="psec reveal">
      <div class="psec-head"><span class="mono-label">{label}</span><h2>{title}</h2></div>
      <div class="psec-body">{body}</div>
    </section>'''
def ul(items): return '<ul class="plist">'+''.join(f'<li>{x}</li>' for x in items)+'</ul>'
def btn(t,u,primary=False): return f'<a class="btn {"btn-primary" if primary else "btn-ghost"}" href="{u}" target="_blank" rel="noopener">{t}</a>'

P=[]
LI='../assets/img/liminal/'
P.append(dict(slug='liminal-umbrella', title='Liminal Umbrella', label='Northwestern MaDE Capstone', img='liminal-umbrella.webp',
  problem="Passengers entering vehicles struggle to close and contain wet umbrellas, leading to messes, extra effort, and limited control.",
  summary="A self-closing, self-containing umbrella that removes the reach-and-pull motion behind every umbrella's worst moment: getting in the car.",
  btns=[], body=
  '<section class="psec reveal"><div class="psec-head"><span class="mono-label">01</span><h2>Ideal user journey</h2></div><div class="psec-body"><p>Walk up, open the door, close the umbrella with one hand, and sit down dry.</p></div></section>'+
  f'<figure class="wide-fig reveal"><img src="{LI}journey.webp" alt="Ideal user journey sketches" loading="lazy"></figure>'+
  '<section class="dev reveal"><div class="psec-head"><span class="mono-label">02</span><h2>Inside the prototype</h2></div></section>'+
  '<div class="dev-stack" data-stack>'+''.join(f'''<div class="dev-step"><figure class="dev-media"><span class="ringwrap"><img src="{LI}{img}.webp" alt="{t}" loading="lazy"></span></figure><div class="dev-text"><span class="dev-num">{n:02d} <i>/ 05</i></span><h3>{t}</h3><p>{d}</p></div></div>''' for n,(t,d,img) in enumerate([
    ('Canopy','A custom pleated canopy that folds down cleanly and predictably.','canopy'),
    ('Ratchet handle','A ratchet and pawl inside the handle, linked to the umbrella button, so closing can happen in small pulls.','ratchet'),
    ('Pull string','A braided cord transmits the force, and a 2:1 pulley halves the pull needed.','pull-string'),
    ('Pull handle','An adjustable locking tab secures the pull string at the handle.','pull-handle'),
    ('Container','A slim container mounts to the handle to hold the wet canopy.','container')],1))+'</div>'+
  '<section class="specs reveal"><div class="psec-head"><span class="mono-label">03</span><h2>Meeting specs</h2></div>'+
  '<div class="spec-big"><div><strong>0 in</strong><span>upper-shaft reach<br>target &le; 21 in</span></div><div><strong>20.15 N</strong><span>maximum pull force<br>target &le; 34 N</span></div><div><strong>90&deg;</strong><span>pull direction<br>ideal 90&deg;</span></div></div>'+
  '<table class="spec-table"><thead><tr><th>Metric</th><th>Marginal</th><th>Ideal</th><th>Prototype</th></tr></thead><tbody>'+
  ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in [('Pull direction','45&ndash;135&deg;','90&deg;','90&deg;'),('Reach (in)','&le; 24','&le; 21','0'),('Pull force (N)','&le; 40','&le; 34','20.15'),('Closed dia. (in)','&le; 3','&le; 3','3'),('Open dia. (in)','&le; 18','&le; 10','11.8')])+
  '</tbody></table></section>'+
  f'''<section class="lbrand reveal"><div class="psec-head"><span class="mono-label">04</span><h2>Branding</h2></div>
  <div class="brand-board"><img class="brand-mark" src="{LI}wordmark.webp" alt="Liminal wordmark">
  <div class="swatches">{''.join(f'<div class="sw" style="--c:{c}"><i></i><b>{n}</b><span>{c}</span></div>' for n,c in [('Black','#000000'),('White','#FFFFFF'),('Liminal Grey','#A2A2A2'),('Liminal Blue','#3A73EC')])}</div>
  <p class="brand-type"><span class="mono-label">Typography</span>Libertinus Serif, &minus;2% letter spacing</p></div></section>'''))

P.append(dict(slug='whifflewash', solx='<div class="sol-extra focus">'+fig(W('40197e43fb6a4f8f9f9134e8b71c6bd3.png',600),'WhiffleWash logo','logo-ring','Logo')+fig(W('4fd2f6aba5c74a99a0fc0cc81238d413.png',900),'WhiffleWash prototype','','Prototype')+fig(W('cc50744aa8d045968aea19249d13dfc0.png',900),'WhiffleWash prototype, open','','Prototype, open')+'</div>', title='WhiffleWash', label='White Space Project', img='whifflewash.webp',
  problem="Laundry pods don't always dissolve. They stick to clothes or get trapped in the drum, and the whole wash fails.",
  summary="A laundry pod container that makes sure pods fully dissolve and clothes get washed as intended.",
  btns=['<a class="btn btn-ghost" href="#infomercial">Watch infomercial</a>'],
  body=
  f'<section class="psec reveal" id="infomercial"><div class="psec-head"><span class="mono-label">Video</span><h2>Infomercial</h2></div><div class="psec-body">{video('hu0lFQHs9JY','WhiffleWash infomercial')}</div></section>'+
  sec('01','The problem, up close', '<p>One or both of these make a wash cycle ineffective:</p>'+ul(['The pod doesn\'t fully dissolve and gets stuck on clothes.','The pod gets trapped in the washing machine drum.'])+imgs('e55fa2153e2f4ed3ad35e5f74ea6931f.jpg 72d2876967074dddb6c2288d151a3d80.png c70f6595048f4105bcdeb693b390ea63.jpg 744e224cf0ed46debc5721f59a2f42fc.png',4,'Undissolved laundry pods','circles'))+
  sec('02','Ideation', '<p>We tested how Tide Pods dissolve using two methods: cold water dissolution and spiking.</p>'+ul(['The blue (whitener) section is the hardest to dissolve.','A 2 cm long, 1.5 cm wide spike alone doesn\'t guarantee dissolution.'])+imgs('51e77537ca2f4c648886955bf24ad704.png a9948c1a244b495a9ef32b254769d073.png',2,'Dissolution testing','small'))+
  '<section class="dev reveal"><div class="psec-head"><span class="mono-label">03</span><h2>Development</h2></div></section>'+
  '<div class="dev-stack" data-stack>'+''.join(f'''<div class="dev-step"><figure class="dev-media{' ring' if img.startswith('c40251') else ''}"><span class="ringwrap"><img src="{W(img,1400)}" alt="{t}" loading="lazy"></span></figure><div class="dev-text"><span class="dev-num">{n:02d} <i>/ 06</i></span><h3>{t}</h3><p>{d}</p></div></div>''' for n,(t,d,img) in enumerate([
     ('Whiffle ball mockup','The base idea: water flows through for dissolution while the pod stays enclosed, away from clothes.','177e028357684a59a2d33a03285a786b.png'),
     ('Linear holes and threads','Evenly spaced holes for water flow, plus threads as a cheap, simple, sustainable lock.','856e391ecc4e450d9460698c093141b9.png'),
     ('Tall thin protrusions','Added the spiking idea inside the ball to agitate the pod during the wash.','588e4bf9325f4fb285ebdfab22f73437.png'),
     ('Conical protrusions','Cone shapes for more contact area, easier printing, and more strength.','ce964329b2874f80b72edfd8d9dcc4d9.png'),
     ('Tighter spacing','Holes and protrusions packed closer for more flow and agitation. Holes resized to 0.6 and 1 cm based on testing, so less detergent escapes.','5710b969bef94e5792db79cfebe7af3a.png'),
     ('Material change','Switched to TPU for flexibility and less noise. The pod now drops in from the top instead of twisting the halves apart. Holes and spikes tuned through factorial testing.','c40251ea7579428bb92d9687e5873bb4.png')],1))+'</div>'
+'<section class="specs reveal"><div class="psec-head"><span class="mono-label">Results</span><h2>Meeting specs</h2></div><div class="specs-row"><div class="spec-big"><div><strong>30% &rarr; 0%</strong><span>pods stuck on clothes</span></div><div><strong>10% &rarr; 0%</strong><span>pods trapped in the drum</span></div><div><strong>10 / 10</strong><span>full dissolution with WhiffleWash</span></div></div><figure class="result-shot"><img src="../assets/img/ww/residue-caught.webp" alt="Undissolved pod residue caught inside the WhiffleWash ball" loading="lazy"><figcaption class="mono-label">Caught inside the ball,<br>not your clothes</figcaption></figure></div><table class="spec-table"><thead><tr><th>Metric</th><th>Marginal</th><th>Ideal</th><th>Prototype</th></tr></thead><tbody><tr><td>Stuck on clothes</td><td>&le; 10%</td><td>0%</td><td>0%</td></tr><tr><td>Trapped in drum</td><td>&le; 5%</td><td>0%</td><td>0%</td></tr><tr><td>Full dissolution</td><td>8 / 10</td><td>10 / 10</td><td>10 / 10</td></tr><tr><td>Hole size (cm)</td><td>&lt; 1.5</td><td>&le; 1.0</td><td>0.6&ndash;1.0</td></tr><tr><td>Wall (mm)</td><td>&ge; 4</td><td>&ge; 6</td><td>6</td></tr></tbody></table></section>'))

P.append(dict(slug='oscar', title='OSCAR: 3D Model Validation Tool', label="Shriners Children's Hospital", img='oscar.webp',
  problem="Shriners Children's Hospital needed a reliable way to check the accuracy of its 3D motion-capture system.",
  summary="A 3D modeling calibration tool built to validate a 3D motion-capture system.",
  btns=[], body=
  sec('01','How it works', split(ul(['Sized like a 7-year-old&rsquo;s skeleton, with reflective markers at the pelvis and clavicle.','Six lockable universal joints move in all three planes.','Geared dials read each joint angle, so the team knows the true value to compare against.']), fig('../assets/img/oscar-ujoint.webp','Lockable universal joint with angle gear')))+
  '<section class="specs reveal"><div class="psec-head"><span class="mono-label">02</span><h2>Meeting specs</h2></div><div class="spec-big"><div><strong>5&deg;</strong><span>angle resolution</span></div><div><strong>360&deg;</strong><span>transverse range</span></div><div><strong>6</strong><span>lockable joints</span></div></div><table class="spec-table"><thead><tr><th>Metric</th><th>Marginal</th><th>Ideal</th><th>Prototype</th></tr></thead><tbody><tr><td>Resolution, sagittal</td><td>5&deg;</td><td>1&deg;</td><td>5&deg;</td></tr><tr><td>Resolution, frontal</td><td>5&deg;</td><td>1&deg;</td><td>5&deg;</td></tr><tr><td>Resolution, transverse</td><td>10&deg;</td><td>1&deg;</td><td>10&deg;</td></tr><tr><td>Range, sagittal</td><td>127.5&deg;</td><td>&gt; 127.5&deg;</td><td>208&deg;</td></tr><tr><td>Range, frontal</td><td>89&deg;</td><td>&gt; 89&deg;</td><td>208&deg;</td></tr><tr><td>Range, transverse</td><td>140&deg;</td><td>&gt; 140&deg;</td><td>360&deg;</td></tr></tbody></table></section>'
))

P.append(dict(slug='one-handed-controller', title='One-Handed PS4 Controller', label='Shirley Ryan AbilityLab', img='ps4-controller.webp',
  problem='After a stroke, 16-year-old Hector could only use his left hand, and a standard controller put half of FIFA out of reach.',
  summary="An adaptive controller for Hector, a 16-year-old stroke survivor, so he could play FIFA again with his left hand. This is the final design we gave him.",
  btns=[],
  body=
  sec('01','The user', split(ul(["After his stroke, Hector has limited motor control in his right arm and leg, so he plays with his left hand only.","He can't reach all the buttons and triggers he needs in FIFA, which hurts his gameplay and is frustrating.","Goal: get him back to his previous level of play and enjoyment."]),
      '<div class="collage">'+fig(W('b833464237f74ef3a2f6c9039542aea7.png',1000,'x_0,y_955,w_1170,h_625'),'Hector playing one-handed')+fig(W('55a42e28dfe84288b787115019d4224f.png',1000,'x_0,y_955,w_1170,h_625'),'Hector holding the controller')+'</div>'))+
  sec('02','Final design', '<p>Levers on an axis of rotation, held by a clamp, let Hector press the right face buttons with his left hand like extra triggers. A weighted stand holds everything steady.</p><ol class="parts"><li><a href="#clamp">Clamp and band</a></li><li><a href="#levers">Accessibility levers</a></li><li><a href="#stand">Stand</a></li></ol>')+
  '<div class="dev-stack ps4-stack" data-stack>'+''.join(f'''<div class="dev-step" id="{sid}"><figure class="dev-media duo-media">{''.join(f'<img src="{W(im,900)}" alt="{t}" loading="lazy">' for im in ims.split())}</figure><div class="dev-text"><span class="dev-num">2.{n}</span><h3>{t}</h3><ul class="plist">{''.join(f'<li>{x}</li>' for x in pts)}</ul></div></div>''' for n,(sid,t,ims,pts) in enumerate([
    ('clamp','Clamp and band','7607658ee5194926a2f4e1c18f8b03d6.png ddff0ee936b840b58b4e17070e86bb99.png',['3D printed PLA clamp holds the levers on their axis.','Fits between triggers and joysticks without blocking a button.','A center rod acts as the axis, tuned in user testing.']),
    ('levers','Accessibility levers','93c88523bdf34f4cb63766b77dffd8ed.png 69192538e3334ecfa486fc79dbe2a75a.png',['Four levers behind the controller press the right face buttons.','Sprint moves to L2, so more fingers stay in play.','Filleted, wider ends for strength and consistent presses.']),
    ('stand','Stand','60f1a7fbbf974df1892600f4909eac17.png',['Short, weighted mic stand matched to his grip.','1.02 lb base keeps it steady mid-game.','180 degree rotation and adjustable height from testing feedback.'])],1))+'</div>'+
  '<section class="specs reveal"><div class="psec-head"><span class="mono-label">Results</span><h2>Meeting specs</h2></div><div class="spec-big"><div><strong>4.0 / 5</strong><span>access to buttons</span></div><div><strong>4.0 / 5</strong><span>ergonomics</span></div><div><strong>0 mm</strong><span>target controller movement, held by a weighted stand</span></div></div><table class="spec-table"><thead><tr><th>Metric</th><th>Marginal</th><th>Ideal</th><th>Prototype</th></tr></thead><tbody><tr><td>Buttons reached</td><td>3 / 4</td><td>4 / 4</td><td>4 / 4<small>via levers</small></td></tr><tr><td>Button access</td><td>3 / 5</td><td>5 / 5</td><td>4.0 / 5<small>sprint on L2</small></td></tr><tr><td>Ergonomics</td><td>3 / 5</td><td>5 / 5</td><td>4.0 / 5<small>fitted stand</small></td></tr><tr><td>Comfort</td><td>3 / 5</td><td>5 / 5</td><td>3.5 / 5<small>adjustable height</small></td></tr><tr><td>Stand rotation</td><td>90&deg;</td><td>180&deg;</td><td>180&deg;<small>weighted base</small></td></tr></tbody></table></section>'+
  sec('03','Orthographic views', '<div class="ortho2 focus">'+''.join(fig(W(f,1400),'Orthographic view of full assembly','',f'View 0{k+1}') for k,f in enumerate('f01cb47383814bd59799c06a5e1d4696.png 789629b0696e41bb8c0323ccf29a1329.png 61f67611447b46dfa3bf42095a0194ac.png 88270d5e5afe4c9eac00011599b5f310.png'.split()))+'</div>')
))

P.append(dict(slug='arm-rehab', title='Arm Rehabilitation Machine', label='Chulalongkorn University AI Lab', img='arm-rehab.webp',
  problem="Robotic arm rehabilitation speeds stroke recovery, but machines like MIT's InMotion cost more than most clinics can afford.",
  summary="A low-cost arm rehabilitation machine inspired by MIT's InMotion ARM. I designed the handle.",
  btns=[], body=
  sec('Overview','Overview', "<p>I worked as a research assistant with Dr. Ronnapee Chaichaowarat at Chulalongkorn University's AI Lab, designing the handle for a low-cost arm rehabilitation machine inspired by MIT's InMotion project.</p>")+
  sec('02','Base design', '<p>Orthographic and isometric CAD views.</p>'+imgs('9070b65765054e5b802f943528a8dd4e.png 7c0c63ebe68840488ef60eb6a90c31c2.png 93f1e5d63160463a9512a4e6256e3afc.png base-front.png',4,'Base CAD views','even box-wide two'))+
  sec('03','Handle design', imgs('d0ee1c55507148aa9625c8f713aab0e2.jpg 4a46e8fccf054e509e14bccdc038667c.png handle-side.png handle-top.png f5dc07ffd83044898d8d9670c5ae8988.jpg',5,'Handle design','even box-tall five'))
))

P.append(dict(slug='surf-chair', title='Surf Chair', label='Furniture Design, Copenhagen', img='surf-chair.webp',
  problem='Everyone started with the same mass-produced plywood chair. The challenge: turn a factory standard into something that feels like the coast.',
  summary="A handcrafted plywood lounge chair inspired by the flow of a surfboard and Nordic design.",
  btns=[], body=
  sec('Overview','Design', "<p>Ergonomic angles and a flexible backrest make it comfortable and durable. The warm beige finish and visible wood grain bring to mind sand and sea. It's light and portable, so it works indoors or out.</p>"+imgs('365baf82cdf848f0b253d0cfa673cab6.jpg 887bbeea009a4d7e9f1a9e967962f82e.jpg 1a1bd720d5224772b0e80073c878ec97.jpg',3,'Surf Chair','even box-sq'))+
  sec('Process','Preliminary sketches', imgs('cdedd622541d4e52abb3d8658d58a25c.png 0acfd66709bd4873b00e20c52cebfdf7.png c56c15685b884a97bd213ad5c5bce7df.png sketch4.png sketch5.png',3,'Preliminary sketches','even box-sq'))
))

P.append(dict(slug='architectural-design', title='Architectural Design', label='Study abroad, Denmark and Sweden', img='architectural-design.webp', cover=True,
  summary="Two hand-drawn projects from an architecture core course and electives in New Nordic Design and Furniture Design. Every drawing here is by hand.",
  btns=[], body=
  '<section class="arch-proj reveal"><div class="arch-head"><span class="mono-label">Project 01</span><h2>TR&Aring;RAMMEN Pavilion</h2>'+
  "<p class='arch-text'>A pavilion in the park next to the SMK museum, inspired by Rodin's <em>The Head of Sorrow</em> and Utzon's Can Lis. A calm wooden structure frames the sculpture against trees and a pond, while large natural rocks serve as seating and lead visitors out into the landscape. Light shifts across the space through the day and hits the sculpture at noon.</p>"+'</div>'+
  '<div class="pav focus">'+'<div class="pv-pair">'+fig(W('89124fa8255b432cbb1379733fe1a6d9.png',1600),'Pavilion plan','pv-a','Plan')+fig(W('372ee243775344b987982f11591fe113.png',1600),'Pavilion elevation and section','pv-b','Elevation and section')+'</div>'+fig(W('13da2d83d3184379817cc9c41ce00761.png',1600),'Pavilion lighting diagram','pv-c','Lighting diagram')+fig(W('db6df9794b70468387337bac4b136805.png',900),'Sculpture sketch','pv-d','Sculpture study')+fig(W('7b2d6afc52c34dd1af60969d4ae08728.png',900),'Sculpture sketch','pv-e','Sculpture study')+'</div>'
  '</section>'+
  '<section class="arch-proj reveal"><div class="arch-head"><span class="mono-label">Project 02</span><h2>The Living Room Culture House</h2>'+
  ("<p class='arch-text'>The living room of N&oslash;rrebro, built into Hans Tavsens Plads park with a public path running through it. Site analysis of foot traffic, demographics, and sun paths shaped the plan.</p><p>A cooking school sits 90 cm below ground for focus, a sheltered zone leads up to a street-level caf&eacute;, and gardens, workspaces, and a fireplace make it a neighborhood gathering place.</p>")+'</div>'+fig(W('e3f8bff0fbde4897a1fefaebf0ed4706.png',1400),'Culture house poster','ch-poster')+
  '<span class="mono-label arch-sub">Drawings</span>'+'<div class="ch-set focus">'+fig(W('0468515a088c4a458b6315d6b2aa94e0.png',1600),'Culture house perspective','ch-persp','Perspective')+fig('../assets/img/arch/ch-model-aerial.webp','Culture house model, aerial view','ch-m1','Model, aerial view')+'</div>'+
  '<div class="plans focus">'+fig(W('9df7c971b7a44758b01bf02480a353ee.png',1800),'Culture house floor plan','pl-floor','Floor plan')+fig(W('4157e4608e4743b89486fc2807bdd576.jpg',1600),'Culture house site plan','pl-site','Site plan')+fig(W('2e6f6634d8b740859e9274eeb40e1200.jpg',1800),'Culture house section','pl-s1','Section A')+fig(W('d096c0bd26794eb9b84eebc7b6eecd24.jpg',1800),'Culture house section','pl-s2','Section B')+'</div>'+
  strip('5682c17f011f4dc996adca54a0a730e4.jpg bb4b603af5164f9cb784e0b7f541563a.png f6a9caff1c234fa990585501cba2444d.jpg 94879fede5bd41caa6d8b958e77995b8.png dc0ee5ba92314f8fbc6f9f20dab64aa5.jpg','Culture house site analysis and interiors','Site analysis and interiors')+'</section>'+
  '<section class="arch-proj reveal"><div class="arch-head"><span class="mono-label">Workshop</span><h2>Model Making</h2><p class="arch-text">Physical models built to test form, light, material, and landscape at small scale.</p></div>'+
  '<div class="models focus">'+fig('../assets/img/arch/model-landscape.webp','Landscape study','md1','<b>01</b> Landscape study')+fig('../assets/img/arch/model-form.webp','Form study','md2','<b>02</b> Form study')+fig('../assets/img/arch/model-texture.webp','Texture study','md3','<b>03</b> Texture study')+fig('../assets/img/arch/model-roofs.webp','Roof studies','md4','<b>04</b> Roof studies')+fig('../assets/img/arch/model-enclosures.webp','Enclosure studies','md5','<b>05</b> Enclosure studies')+'</div></section>'+
  '<section class="arch-proj reveal"><div class="arch-head"><span class="mono-label">Sketchbook</span><h2>Sketches</h2></div>'+
  bento('efee5c7dc3624009950a98a10db5ac8a.png b02269c5b4a1431f9f9ed4fc3e21e849.png 05bc342935a043a6a19db6a01e401dd6.png aca41a74e47844df9a6a6834237062e3.png sk-plants.png','wall six focus','Architectural sketch')+'</section>'
))

P.append(dict(slug='industrial-design', title='Industrial Design', label='Sketches and concepts', img='ind/a2c0a98e01e941d9862bf4da6466e25a.webp', cover=True,
  summary="Four product studies, each taken from thumbnails and working drawings to a final concept.",
  btns=[], body=''.join(
    f'''<section class="ind reveal"><div class="ind-head"><span class="ind-num">{n}</span><h2>{t}</h2><p>{d}</p></div>'''
    + '<div class="final-set n'+str(len(final.split()))+' focus"><span class="final-num" aria-hidden="true">'+n+'</span><span class="mono-label final-label">Final concept</span>'+''.join(fig(W(f,1600),t+' final concept','fs'+str(k)) for k,f in enumerate(final.split()))+'</div>'
    + ('<div class="ideas focus">'+''.join(f'<div class="idea"><span class="mono-label">{il}</span><div class="idea-imgs">'+''.join(fig(W(f,900),t+' idea') for f in ifs.split())+'</div></div>' for il,ifs in ideas)+'</div>' if ideas else '')
    + (strip(proc, t+' process sketch', 'Thumbnails and working drawings') if proc else '')
    + '</section>'
    for n,t,d,final,fc,ideas,proc in [
     ('01','Northwestern Bus Stop','Two directions, Zen and Organic Modernism, developed into a final concept.',
      '5b596562019c4c0b93f3bff4440836f5.png e879d716f0104552980109b5d38f7e17.png','duo2',
      [('Idea 01: Zen','62f34abc7b4d41eab9c014c2eeed8b3e.png 832f0b41f4814688b6242cce7e6beb83.png'),('Idea 02: Organic Modernism','4cc53e96dfb44eca9848c0df3b7a80ad.png 0a8cbc17a8fe46028c9c5177f0108263.png')],
      '529b31ac137247ec8adafd941f01922a.png ddc8bab626d34540a091a131a1eefd80.png 16dbbcd326b84071ad3a918296419b7a.png 5f758b985f8647dc931defb88980907d.png 4b87d34981d641b091da4841201571c3.png 305992c11aee49e988087acdbeaf04e1.png 1634382e2ec54ab58a172de0e18880d9.png fadd4dc943a14846b4ebaa970691121b.png 610633e8242d41318445a973b7727ccd.png 228923a3712c4297a26c0d6f218e73dc.png 33a5678309c2435089c070c8ed387133.png 5543586c803d4db0a51ca48d68b22689.png'),
     ('02','Space-Efficient Furniture','Two directions, Eames style and outdoor camping, developed into a final concept.',
      '708d7574b874478b9311446f6da43147.png 9ccc6ed6757142a7a38c5e19d8fc8d0e.png a2c0a98e01e941d9862bf4da6466e25a.png be4ca461c7024f179e70504130eebafd.png','quad',
      [('Idea 01: Eames style','56da038cba2f409fbb55e24501b887fe.png'),('Idea 02: Outdoor and camping','6b2ec448b7ed4f0db88ed52b4896d951.png b691b56b4e6a42c2a111f961289ba0af.png')],
      '0acc042adc0748aa968522c0fe840ebe.png 04c60f8435864d50afff8501a1c27955.png dce61b286ff6416bb86009251c5df272.png eb8bb14948ec41f7ac37c87714ecc91e.png 798392b72e59419e8bd454b9a98931ff.png feb23c9f7e1243e38c863f7e4a2319d1.png 7682c35f544146a499497c21b45d9b44.png 7ab0b98781e042fa9198a71c3580a1aa.png 54e4ba63cc074ca3944589c520d9e862.png 857f6de3009e429cbe6025631c6b3c25.png 87f6050ffd654fd4aa511a5099a3a816.png 1275e535f0994826969cd0a3b9a7a9b5.png 41a3f70764b34b3b937db0ab36309a39.png abdc11835fec42ada88de5a4a5e7174e.png b83480aa903c4ce98bf529a64161bab2.png'),
     ('03','Hiking Boots','From a page of thumbnails to a detailed boot with tread and material studies.',
      '954be03392e74d3ba660ca0f9a2f7414.png 3d5cb70fd3604e8ba93c57c3cbb899dd.png','duo2', [],
      '62ef8429d84c4d729b220f38bab43a8f.png 0b854f5c84a046d3a8a7eecdd1f796b9.png 0c4735e2e1d54362b619abcd9402b3d9.png ef40b761fcbe4bf0933e0f7e54ced716.png 78c3f1de06ff43dfa07c917f4e1c3fe0.png 581fd097a8ba4f54b2094f86a9d2f058.png 14f0fcd3956c45a78905e03adec15c14.png 1013ce9be9e0428e9794238032cce509.png 4b5c4be378d7488dbc7f469d905947d6.png 01c866ac73c142879b39aa2e19df7c46.png bc4dae38e23242cba92472108691fc91.png db5feb337be948479674554439cee40a.png 71a2c13349644c80b1607c1e91142022.png cf8336bd075447ea85d6ff09f5d1bf2e.png'),
     ('04','Multi-Purpose Bags','Working drawings for bags that adapt to different uses.',
      '2259ad2728594063a88cc991fcc44d33.png c627115361cc45ae918ee18185f2b0fc.png 5ff50d7ee9c04516b51698b600b40d2a.png b24a68b2451e467bb42e59abcf0c5d1f.png','quad', [], ''),
    ])
))

ST={'liminal-umbrella': ('Closing and stowing a wet umbrella while getting into a car is messy, awkward, and hard to control.', 'A handle that closes the umbrella from the grip. Pull, ratchet, done, with no reach up the wet shaft.', '../assets/img/liminal/prototype.webp'), 'whifflewash': ("Laundry pods don't always dissolve. They stick to clothes or get trapped in the drum, and the whole wash is wasted.", 'A Whiffle ball container that agitates the pod and floods it with water, so it fully dissolves and never touches your clothes.', W('4de7dcc3a37f463786779f435e3976c8.png',1800)), 'oscar': ("Shriners Children's Hospital needed a reliable way to check the accuracy of its 3D motion-capture system.", "OSCAR, a child-sized model with lockable, angle-marked joints. Set a pose, read the true angles, and compare them to what the system reports.", '../assets/img/oscar.webp'), 'one-handed-controller': ('Hector wanted to play his favorite game, FIFA, again. After a stroke, he only had one working hand.', 'A clamp-on lever system that brings every right-side button to his left hand, held steady on an adjustable stand.', W('f01cb47383814bd59799c06a5e1d4696.png',1800)), 'arm-rehab': ("Robotic arm therapy helps stroke patients recover movement, but machines like MIT's InMotion are priced beyond most clinics.", 'A low-cost rehabilitation machine, with a handle I designed around the grip a recovering patient actually has.', ''), 'surf-chair': ('Everyone got the same factory-made plywood chair. Our job: give it a story.', 'The flat plywood reshaped into the flowing curve of a surfboard: light enough to carry to the beach, comfortable enough to stay.', '')}
head=open(f'{ROOT}/projects.html').read()
start=head.index('<header class="site-header">'); end=head.index('</header>')+9
header=head[start:end].replace('href="','href="../').replace('href="../http','href="http').replace(' class="active"','')
header=header.replace('<li><a href="../projects.html">','<li><a href="../projects.html" class="active">')
fs=head.index('<footer'); fe=head.index('</footer>')+9
footer=head[fs:fe].replace('href="','href="../').replace('href="../http','href="http').replace('href="../mailto','href="mailto')

for k,p in enumerate(P):
    nxt=P[(k+1)%len(P)]
    cover=' cover' if p.get('cover') else ''
    btns=f'<div class="pactions">{"".join(p["btns"])}</div>' if p['btns'] else ''

    if p['slug'] in ST:
        prob,sol,simg=ST[p['slug']]
        solfig=f'<figure class="sol-media"><img src="{simg}" alt="{html.escape(p["title"])} final design" loading="lazy"></figure>' if (simg and p['slug']!='oscar') else ''
        hero=f'''    <header class="shero">
      <a class="pback mono-label" href="../projects.html">&larr; All projects</a>
      <div class="shero-grid">
        <div class="shero-text reveal">
          <span class="mono-label">{html.escape(p['label'])}</span>
          <h1>{p['title']}</h1>
          <span class="mono-label shero-plabel">The problem</span>
          <p class="shero-problem">{html.escape(prob)}</p>
          {btns}
        </div>
        <figure class="shero-media reveal reveal-delay-1"><img src="{'../assets/img/'+p['img']}" alt="{html.escape(p['title'])}"></figure>
      </div>
    </header>
    <section class="solution reveal s-{p['slug']}">
      <span class="mono-label">The solution</span>
      <p class="sol-text">{html.escape(sol)}</p>
      {solfig}
      {p.get('solx','')}
    </section>'''
    else:
        hero=f'''    <header class="phero{' has-problem' if p.get('problem') else ''}">
      <a class="pback mono-label" href="../projects.html">&larr; All projects</a>
      <div class="phero-grid">
        <div class="phero-text reveal">
          <span class="mono-label">{html.escape(p['label'])}</span>
          <h1>{p['title']}</h1>
          {('<p class="pproblem"><span class="mono-label">The problem</span>'+html.escape(p['problem'])+'</p><p class="lede">'+html.escape(p['summary'])+'</p>') if p.get('problem') else '<p class="lede">'+html.escape(p['summary'])+'</p>'}
          {btns}
        </div>
        <div class="phero-media{cover} reveal reveal-delay-1"><img src="{p['img'] if p['img'].startswith('http') else '../assets/img/'+p['img']}" alt="{html.escape(p['title'])}"></div>
      </div>
    </header>'''
    doc=f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{p['title']} | Tanik (Nick) Visuthikosol</title>
<meta name="description" content="{html.escape(p['summary'])}">
<link rel="stylesheet" href="../css/style.css?v=61">
</head>
<body class="project-page p-{p["slug"]}">

{header}

<main>
  <article class="wrap">
{hero}
    {p['body']}
    <a class="pnext" href="{nxt['slug']}.html"><span class="mono-label">Next project</span><strong>{nxt['title']} &rarr;</strong></a>
  </article>
</main>

{footer}

<div class="lightbox" hidden><button class="lb-close" aria-label="Close">&times;</button><img alt=""></div>
<script src="../js/main.js?v=61"></script>
</body>
</html>
'''
    os.makedirs(f'{ROOT}/work',exist_ok=True)
    open(f'{ROOT}/work/{p["slug"]}.html','w').write(doc)
print('ok', len(P))

# consistent section numbering on product pages
import re as _re, glob as _g
for _f in _g.glob(ROOT+'/work/*.html'):
    if _f.endswith(('architectural-design.html','industrial-design.html')): continue
    _t=open(_f).read(); _n=[0]
    _t=_t.replace('id="infomercial"><div class="psec-head"><span class="mono-label">','id="infomercial"><div class="psec-head"><span class="mono-label vid">')
    def _r(m):
        _n[0]+=1; return m.group(1)+f'{_n[0]:02d}'+m.group(2)
    _t=_re.sub(r'(<div class="psec-head"><span class="mono-label">)[^<]*(</span><h2>)',_r,_t)
    open(_f,'w').write(_t)
