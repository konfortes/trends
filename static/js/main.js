var app = new Vue({
    el: '#app',
    data: function() {
        return {
            newKeyword: "",
            keywords: [],
            tracking: false
        };
    },
    methods: {
        addKeyword: function(event) {
            if (this.newKeyword && this.newKeyword.length > 0) {
                this.keywords.push(this.newKeyword);
                this.newKeyword = "";
            }
        },

        clearKeywords: function(){
            this.keywords = [];
        }, 

        startTracking: function(){
            axios.post('trends/api/v1/track_keywords', {keywords: this.keywords})
                .then(()=> {
                    this.tracking = true;
                    var ctx = document.getElementById("myChart").getContext('2d');
                    drawChart(ctx);
                })
            ;
        }
    }
});


function drawChart(ctx){
    axios.get('/trends/api/v1/trends')
        .then(handleResponse)
        .then((chartData) => {
            refreshChart(ctx, chartData);
        });

    setTimeout(drawChart, 10000)
}

function handleResponse(response) {
    return {
        labels: response.data.map(t => t.name),
        scores: response.data.map(t => t.score)
    }
}

function refreshChart(ctx, data) {
    let myChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: data.labels,
            datasets: [{
                label: 'trends',
                data: data.scores,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgb(204, 201, 96)',
                    'rgb(167, 224, 132)',
                    'rgb(36, 33, 206)',
                    'rgb(135, 226, 211)'
                ]
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }],
                xAxes: [{
                    ticks: {
                        autoSkip: false
                    }
                }],
            }
        }
    });
}