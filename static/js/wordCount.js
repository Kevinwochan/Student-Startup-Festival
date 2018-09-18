function wordCount( text ){
	var wordCount = text.match(/\S+/g)
	return wordCount;
}

function onInput( wordLimit , textarea, counter){
	var wordsCounted = wordCount( textarea.val());
	counter.text( counter.text().replace( /[0-9]+/, wordLimit - wordsCounted ) );
}

var textarea = $(".word-count")[0];
var counter = $(".word-counter")[0];
console.log(counter);
var wordLimit = counter.text().match(/[0-9]+/);
console.log(textarea);
console.log(wordLimit);
textarea.addEventListener("input", onInput( wordLimit ,textarea, counter), false );
