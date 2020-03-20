console.log("yup, at least theres JS")
$(function () {

    $('button').on('click', function (evt) {
        evt.preventDefault();
        console.log(evt.target.previousElementSibling.value);
        // $user_guess = $("#guess").value();
        user_guess = evt.target.previousElementSibling.value
        await askingServer(user_guess)
    })
    async function askingServer(user_guess){
        // sending request to server to see 
        // if it's a playable word
        response = await axios.get('http://localhost:5000/')
    }    


});


// function takeUserWords(word)
//     // take user word from form name="guess"

//     // send GET request to server
//     // return bool
