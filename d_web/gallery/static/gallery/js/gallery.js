jQuery(document).ready(function($) {

    $('#thumbList').justifiedGallery({
			rowHeight : 120,
			fixedHeight : false,
			captions : false,
			margins : 7,
			sizeRangeSuffixes: {
				'lt100':'_t',
				'lt240':'_m',
				'lt320':'_n',
				'lt500':'',
				'lt640':'_z',
				'lt1024':'_b'
			}
        })
});