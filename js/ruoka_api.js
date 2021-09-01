(function() {
    'use strict';

    moment.locale('fi');
    
    var weekdays = ['maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai'];
    
    var selectedDate = moment(new Date());
        
    var contentElem = document.getElementById('main-content'),
        source = main_template.innerHTML,
        template = doT.template(source),
        apiUrls = 'https:/www.sodexo.fi/ruokalistat/output/daily_json/111/';
        
    updateMenus(selectedDate);  
    
    function updateMenus(date) {
        contentElem.innerHTML = '<h1 id="meme">Meme (TTY)</h1>';
        
        var dateString = date.format('YYYY-MM-DD'),
            requestUrl = apiUrls + dateString;
            
        var req = new XMLHttpRequest();
        
        req.addEventListener('load', function() {
            var context = JSON.parse(this.responseText);
            context.date = weekdays[date.weekday()] + ' ' + date.format('D.M.');
            
            contentElem.innerHTML = template(context);
        });
        
        req.open('get', requestUrl, true);
        req.send();
    }
})();