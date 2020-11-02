//custom pagination design

var current=0;
var total=0;
$(document).ready(function(){

    
    current=1;
    total=Number($('.tot_1').text());


    //progress bar logic
    for(var i=1;i<=total;i++)
    {
        var AreaVal=(100/total)*i;
        $('.bar_'+String(i)).css('aria-valuenow',String(AreaVal));
        $('.bar_'+String(i)).css('width',String(AreaVal)+'%');
    }

    

    //initial condition after loading page
    $('.box_'+String(current)).show();
    for(var i=1;i<=total;i++)
    {
        if(i!=current)
        {
            $('.box_'+String(i)).hide();
        }
    }
    $('.prev').hide();
    

    
    //prev button function
    $('.prev').click(function(){
        current--;


        //logic for showing buttons
        if(current==1)
        {
            $('.prev').hide();
            $('.next').show();
        }
        else if(current==total)
        {
            $('.next').hide();
            $('.prev').show();
        }
        else
        {
            $('.prev').show();
            $('.next').show();
        }
        $('.box_'+String(current)).show();
        for(var i=1;i<=total;i++)
        {
            if(i!=current)
            {
                $('.box_'+String(i)).hide();
            }
        }    
    })


    //next button function
    $('.next').click(function(){
        current++;

        //logic for showing buttons
        if(current==1)
        {
            $('.prev').hide();
            $('.next').show();
        }
        else if(current==total)
        {
            $('.next').hide();
            $('.prev').show();
        }
        else
        {
            $('.prev').show();
            $('.next').show();
        }
        $('.box_'+String(current)).show();
        for(var i=1;i<=total;i++)
        {
            if(i!=current)
            {
                $('.box_'+String(i)).hide();
            }
        }    
    })
    
    
// timer functionality script

    secs = 30*total;        //avg. time per question = 30 sec.
    timer = setInterval(function () {
    var element = document.getElementById("status");
    hh=Math.floor(secs/3600);
    mm=Math.floor(((secs)%3600)/60);
    ss=secs-(hh*3600+mm*60);
    element.innerHTML = hh+":"+mm+":"+ss;
    if(secs < 1){
        clearInterval(timer);
        document.getElementById('myquiz').submit();
    }
    secs--;
}, 1000)

})
