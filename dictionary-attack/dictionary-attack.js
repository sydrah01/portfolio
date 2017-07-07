var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true; 
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false; 
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() 
{
	console.log(wordsList);
	var pw = document.getElementById("pw").value.toLowerCase(); 
	console.log(pw);
	var num = 0;
	for (var x = 0; x < wordsList.length; x++)
	{
		if(pw == wordsList[x])
			{ 
				num =1;
				document.getElementById("results").innerHTML= "Weak password";
				x=wordsList.length;
			}
	}
	if (num==0)
	{
		document.getElementById("results").innerHTML =("good password");
	}
}