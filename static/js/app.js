// function extractCon(s) {
//     let span = document.createElement("span")
//     span.innerHTML = s
//     return span.textContent || span.innerText
// }


function raiseBigImg(whichpic) {
    console.log("raise " + whichpic + " "+html_url)
    let choice = document.getElementById("bigimg");
    let cmt =  document.getElementById("comment");

    choice.className = whichpic;
    document.getElementById("bigimg_anchor").href = html_url;
    //cmt.innerHTML = extractCon("./" + txt);
    //cmt.innerHTML='<object type="text/html" data="/'+html_url+'" ></object>';
    //cmt.innerHTML=akira.innerText;
}

// This code snippet provides an app clock to
// assist app users to monitor their in app work time
//
// Code snippet captured from: 
// https://www.w3schools.com/js/tryit.asp?filename=tryjs_timing_clock

function appClock() {
    const today = new Date();
    let h = today.getHours();
    let m = today.getMinutes();
    let s = today.getSeconds();
    h = zeroPrefix(h);
    m = zeroPrefix(m);
    s = zeroPrefix(s);
    document.getElementById('appClockTxt').innerHTML = h + ":" + m + ":" + s;

    setTimeout(appClock, 1000); // set timer callback for 1000ms
}

function zeroPrefix(i) {
    return ((i < 10) ? ("0" + i) : i);  // add zero in front of numbers < 10
}