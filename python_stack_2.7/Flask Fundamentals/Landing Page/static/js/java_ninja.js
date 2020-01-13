function sayHello5(){

    var hello5 = "just decided to say hello again today";

    for (var idx = 0; idx < 5; idx++){
        console.log(hello5)
    }
}
sayHello5();

var oneTime = ["hello!", "time", "more", "one", "just"];

function cycleHello(arr){
    var helloStr = "";
    
    for (var idx = arr.length - 1; idx >= 0; idx--){
        helloStr += " " + arr[idx];
    }
    console.log(helloStr);
    return helloStr;

}   
cycleHello(oneTime);