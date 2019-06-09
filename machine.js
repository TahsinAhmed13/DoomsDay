// days in months
var days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

function isLeapYear(year) {
    var yearInCent = year % 100;
    if (yearInCent != 0 && year % 4 == 0) {
        return true;
    } else if (yearInCent == 0 && year % 400 == 0) {
        return true;
    }
    return false;
}

function getMaxDays(month, year) {
    if (isLeapYear(year)) {
        days[1] = 29;
    } else {
        days[1] = 28;
    }
    return days[month - 1];
}

function getDate() {
    var month = document.getElementById("month").value; 
    var day = document.getElementById("day").value; 
    var year = document.getElementById("year").value;
    return [month, day, year];     
}

function nextMonth(e) {
    var date = getDate();     
    //up arrow 
    if(e.keyCode == 38) { 
        if(date[0] <= 0) {
            document.getElementById("month").value = 1;
        }else if(date[0] >= 12) {
            document.getElementById("month").value = 1; 
            document.getElementById("year").value = String(Number(date[2]) + 1); 
        }else {
            document.getElementById("month").value = String(Number(date[0]) + 1); 
        }
    //down arrow
    }else if(e.keyCode == 40) { 
        if(date[0] <= 1) {
            document.getElementById("month").value = 12; 
            document.getElementById("year").value = String(Number(date[2]) - 1); 
        }else {
            document.getElementById("month").value = String(Number(date[0]) - 1); 
        }
    //right arrow
    }else if(e.keyCode == 39) {
        var len = document.getElementById("month").value.length; 
        var index = document.getElementById("month").selectionEnd; 
        if(index >= len) {
            document.getElementById("day").focus(); 
        }
    }  

    date = getDate(); 
    if(date[1] > getMaxDays(date[0], date[2])) {
        document.getElementById("day").value = getMaxDays(date[0], date[2]); 
    }
}

function nextDay(e) {
    var date = getDate();  
    //up arrow 
    if(e.keyCode == 38) {
        if(date[0] <= 0) {
            document.getElementById("day").value = 1;
        }else if(date[1] >= getMaxDays(date[0], date[2])) {
            nextMonth(e); 
            document.getElementById("day").value = 1; 
        }else {
            document.getElementById("day").value = String(Number(date[1]) + 1); 
        }
    //down arrow
    }else if(e.keyCode == 40) {
        if(date[1] <= 1) {
            nextMonth(e); 
            date = getDate(); 
            document.getElementById("day").value = getMaxDays(date[0], date[1]); 
        }else {
            document.getElementById("day").value = String(Number(date[1]) - 1); 
        }
    //left arrow 
    }else if(e.keyCode == 37) {
        var index = document.getElementById("day").selectionStart; 
        if(index <= 0) {
            document.getElementById("month").focus(); 
        }
    //right arrow
    }else if(e.keyCode == 39) {
        var len = document.getElementById("day").value.length; 
        var index = document.getElementById("day").selectionEnd; 
        if(index >= len) {
            document.getElementById("year").focus(); 
        }
    }
}

function nextYear(e) {
    var date = getDate(); 
    //up arrow 
    if(e.keyCode == 38) {
        if(date[0] <= 0) {
            document.getElementById("day").value = 1;
        }else {
            document.getElementById("year").value = String(Number(date[2]) + 1); 
        }
    //down arrow
    }else if(e.keyCode == 40 && date[2] > 0) {
        document.getElementById("year").value = String(Number(date[2]) - 1); 
    //left arrow
    }else if(e.keyCode == 37) {
        var index = document.getElementById("year").selectionStart; 
        if(index <= 0) {
            document.getElementById("day").focus(); 
        }
    }
}