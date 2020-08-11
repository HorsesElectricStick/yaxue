function get_option (x) {
    let college = [],
        option, 
        d = [],
        d2 = [],
        o = [];
    for (let i in x.detail) {
        college.push(x.detail[i]);
    }
    for (let i in college) {
        d.push({name: college[i].college_name, icon: 'circle'});
    }
    if (college.length == 1) {
        for (let i in college[0]) {
            if (i == 'college_name') {
                continue;
            } else {
                    o.push({name: i, max:function(t){
                        if (t < 1) {
                            return 1;
                        } else if (t === null){
                            return 10000;
                        } else {
                            if (t.toString()[0] < 5) {
                                return 5 * 10 ** (t.toString().length -1);
                            } else {
                                return 10 ** t.toString().length;
                            }
                        }
                    }(college[0][i])});
                }}
    } else {
        for (let i in college[0]) {
            if (i == 'college_name') {
                continue;
            } else {
                    o.push({name: i, max:function(t1,t2){
                        if (Math.max(t1,t2) < 1) {
                            return 1;
                        } else if (t1 === null && t2 === null){
                            return 10000;
                        } else {
                            if (Math.max(t1,t2).toString()[0] < 5) {
                                return 5 * 10 ** (Math.max(t1,t2).toString().length -1);
                            } else {
                                return 10 ** (Math.max(t1,t2).toString().length);
                            }
                        }
                    }(college[0][i], college[1][i])});
                }}
    }
    for (let i in college) {
        d2.push({
            name: college[i].college_name,
            value: function (x){
                let item = [];
                for (let i in x){
                    if (i == 'college_name') {
                        continue;
                    } else if (x[i] === null){
                        item.push(0);
                    } else {
                        item.push(x[i]);
                    }
                }
                return item;
            }(college[i]),
            label: {                    // 单个拐点文本的样式设置
                normal: {
                    show: true,             // 单个拐点文本的样式设置。[ default: false ]
                    position: 'top',        // 标签的位置。[ default: top ]
                    distance: function(x) {
                        if (i == 0) {
                            return 5;
                        } else {
                            return 15;
                        }
                    } (i),            // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。[ default: 5 ]
                    color: 'auto',          // 文字的颜色。如果设置为 'auto'，则为视觉映射得到的颜色。[ default: "#fff" ]
                    fontSize: 14,           // 文字的字体大小
                    formatter:function(params) {
                        return params.value;
                    }
                }
            }
        });
    }
    option = {
        legend: {
            data: d
        },
        radar: {
            formatter: '{value}',
            center: ['50%', '50%'],
            name: {
                textStyle: {
                    color: '#fff',
                    backgroundColor: '#999',
                    borderRadius: 3,
                    padding: [3, 5],
                    fontSize: 14,
                }
            },
            indicator: o
        },
        series: [{
            name: 'All Beauty College',
            type: 'radar',
            areaStyle: {normal: {opacity: 0.5}},
            itemStyle: {
                normal: {
                    // color: '#a8bcd4',
                    lineStyle: {
                        width: 1
                    },
                },

            },
            data : d2
        }]
    };
    return option
}

function clear_text (id) {
    $('#'+id).val("");
}