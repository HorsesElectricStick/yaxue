function get_option (data) {
    console.log(data.college_name)
    let college_name = Object.keys(data);
    let option = {
        legend: {data: college_name, icon: 'circle'},
        radar: {
            formatter: '{value}',
            center: ['50%', '50%'],
            name: {
                textStyle: {
                    color: '#fff',
                    backgroundColor: '#999',
                    borderRadius: 3,
                    padding: [3, 5],
                    fontSize: 12,
                }
            },
            indicator: [
                { name: '在校', max: 6500}, 
                { name: '全日制', max: 1},
                { name: '非全日制', max: 1},
                { name: 'test3', max: 38000},
                { name: 'test2', max: 52000},
                { name: 'test1', max:30000}
            ]
        },
        series: [{
            name: 'ttttt',
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
            data : [
                {
                    value : [data.student_count, data.full_time, data.part_time, 35000, 50000, 19000],
                    name : 'ttt',
                    symbolSize: 5,
                    label: {                    // 单个拐点文本的样式设置
                        normal: {
                            show: true,             // 单个拐点文本的样式设置。[ default: false ]
                            position: 'top',        // 标签的位置。[ default: top ]
                            distance: 5,            // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。[ default: 5 ]
                            color: 'auto',          // 文字的颜色。如果设置为 'auto'，则为视觉映射得到的颜色，如系列色。[ default: "#fff" ]
                            fontSize: 12,           // 文字的字体大小
                            formatter:function(params) {
                                return params.value;
                            }
                        }
                    },
                },
                    {
                    value : [5000, 14000, 29000, 31000, 42000, 21000],
                    name : 'tttt',
                        label: {                    // 单个拐点文本的样式设置
                            normal: {
                                show: true,             // 单个拐点文本的样式设置。[ default: false ]
                                position: 'top',        // 标签的位置。[ default: top ]
                                distance: 5,            // 距离图形元素的距离。当 position 为字符描述值（如 'top'、'insideRight'）时候有效。[ default: 5 ]
                                color: 'auto',          // 文字的颜色。如果设置为 'auto'，则为视觉映射得到的颜色，如系列色。[ default: "#fff" ]
                                fontSize: 12,           // 文字的字体大小
                                formatter:function(params) {
                                    return params.value;
                                }
                            }
                        },
                }
            ]
        }]
    };
    return option
}