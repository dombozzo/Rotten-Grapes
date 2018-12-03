function REVIEWS_GET_VARIETY(){
    var var_id = document.querySelector('.varId').value;
    var xhr = new XMLHttpRequest()

    url = "http://student04.cse.nd.edu:52087/reviews/" + var_id;
    xhr.open("GET", url, true)

    xhr.onload = function(e){
        console.log(xhr.responseText);
        searchVariety(JSON.parse(xhr.responseText)["data"])
    }

    xhr.onerror = function(e) {
        // searchVariety(xhr.statusText)
    }

    xhr.send(null)
}

function USERS_GET(){
    UID = document.querySelector('.uidSignIn').value
    var xhr = new XMLHttpRequest()

    url = "http://student04.cse.nd.edu:52087/users/" + UID;
    xhr.open("GET", url, true)

    xhr.onload = function(e){
        // console.log(xhr.responseText);
        if (JSON.parse(xhr.responseText)["result"] == "success"){
            signIn(JSON.parse(xhr.responseText)["name"], JSON.parse(xhr.responseText)["twitter"]);
        } else {
            document.querySelector('.errorUid').removeAttribute("hidden");
            // console.log("error uid");
        }
    }

    xhr.onerror = function(e) {
        console.log(xhr.statusText);
    }

    xhr.send(null)
}

function USERS_DELETE(){
    var xhr = new XMLHttpRequest()

    url = "http://student04.cse.nd.edu:52087/users/" + UID;
    xhr.open("DELETE", url, true)

    xhr.onload = function(e){
        console.log(xhr.responseText);
        signOut();
    }

    xhr.onerror = function(e) {
        console.log(xhr.statusText);
    }

    xhr.send(null);
}

function USERS_POST(){
    var xhr = new XMLHttpRequest()
    var name = document.querySelector('.newUserName').value;
    var twitter = document.querySelector('.newUserTwitter').value;

    url = "http://student04.cse.nd.edu:52087/users/";
    xhr.open("POST", url, true)

    xhr.onload = function(e){
        // console.log(xhr.responseText);
        UID = JSON.parse(xhr.responseText)["user_id"];
        signIn(name, twitter);
    }

    xhr.onerror = function(e) {
        console.log(xhr.statusText);
    }

    var payload = {
        "name": name,
        "twitter": twitter
    }
    xhr.send(JSON.stringify(payload))
}

function REVIEWS_POST(bid, score, desc){
    var xhr = new XMLHttpRequest()

    url = "http://student04.cse.nd.edu:52087/reviews/";

    xhr.open("POST", url, true);

    xhr.onload = function(e){
        // console.log(xhr.responseText)
    }

    xhr.onerror = function(e) {
        console.log(xhr.statusText)
    }

    // console.log("description: " + desc.toString())

    var payload = {
        "uid": UID.toString(),
        "bid": bid.toString(),
        "score": score.toString(),
        "description": desc.toString()
    }
    xhr.send(JSON.stringify(payload))
}

function BOTTLES_GET(ev){
    // console.log(ev.target);
    bid = ev.target.id;
    ev.target.setAttribute("hidden", "true");
    var xhr = new XMLHttpRequest()

    url = "http://student04.cse.nd.edu:52087/bottles/" + bid;
    xhr.open("GET", url, true)

    xhr.onload = function(e){
        console.log(xhr.responseText);
        addInfo(bid, JSON.parse(xhr.responseText));
    }

    xhr.onerror = function(e) {
        console.log(xhr.statusText);
    }

    xhr.send(null)
}

function signIn(userName, twitter){
    // API is called and then this changes the HTML that needs to be changed
    document.querySelector('.userSignIn').setAttribute("hidden", "true");
    document.querySelector('.userInfo').removeAttribute("hidden");
    userNameItem = document.querySelector('.userName');
    twitterItem = document.querySelector('.twitter');
    uidItem = document.querySelector('.userUid');
    // console.log(userName);
    // console.log(twitter);
    userNameItem.innerHTML = userName;
    twitterItem.innerHTML = twitter;
    uidItem.innerHTML = "UID: " + UID;
}

function signOut(ev){
    document.querySelector('.userInfo').setAttribute("hidden", "true");
    document.querySelector('.userSignIn').removeAttribute("hidden");
    document.querySelector('.errorUid').setAttribute("hidden", "true");
}

function openNewUserForm(ev){
    document.querySelector('.signInOrNewUser').setAttribute("hidden", "true");
    document.querySelector('.createNewUserForm').removeAttribute("hidden");
}

function createReview(ev){
    var bid = document.querySelector('.createBid').value;
    var score = document.querySelector('.createScore').value;
    var desc = document.querySelector('.createDescription').value;
    REVIEWS_POST(bid, score, desc);
}

function createSingleReviewHTML(review){
    var score = review.score;
    var wineName = review.title;
    var desc = review.description;
    var id = review.id;
    superOverall = document.createElement("div");
    overall = document.createElement("div");
    overall.setAttribute("class", "row singleReview");
    scoreDiv = document.createElement("div");
    scoreDiv.setAttribute("class", "col-1");
    scoreText = document.createElement("h2");
    scoreText.innerHTML = score;
    scoreDiv.appendChild(scoreText);
    overall.appendChild(scoreDiv);
    infoDiv = document.createElement("div");
    infoDiv.setAttribute("class", "col-11");
    nameText = document.createElement("h4");
    nameText.innerHTML = wineName;
    descText = document.createElement("p");
    descText.innerHTML = desc;
    moreInfo = document.createElement('button');
    moreInfo.setAttribute("type", "submit");
    moreInfo.setAttribute("class", "btn btn-outline-info moreInfoButton");
    moreInfo.setAttribute("id", id);
    moreInfo.innerHTML = "More Information";
    infoDiv.appendChild(nameText);
    infoDiv.appendChild(descText);
    infoDiv.appendChild(moreInfo);
    overall.appendChild(infoDiv);
    superOverall.insertAdjacentHTML('beforeend', '<hr/>');
    superOverall.appendChild(overall);
    return superOverall;
}

function addInfo(bid, info){
    targetButton = document.getElementById(bid);
    moreInfoDiv = document.createElement("div");
    moreInfoUL = document.createElement("ul");
    price = document.createElement("li");
    price.innerHTML = "Price: " + info.information.price;
    country = document.createElement("li");
    country.innerHTML = "Country: " + info.information.country;
    winery = document.createElement("li"); 
    winery.innerHTML = "Winery: " + info.information.winery;
    designation = document.createElement("li");
    designation.innerHTML = "Designation: " + info.information.designation;
    province = document.createElement("li");
    province.innerHTML = "Province: " + info.information.province;
    br = document.createElement("br");
    moreInfoUL.appendChild(br);
    moreInfoUL.appendChild(price);
    moreInfoUL.appendChild(country);
    moreInfoUL.appendChild(winery);
    moreInfoUL.appendChild(designation);
    moreInfoUL.appendChild(province);
    moreInfoDiv.appendChild(moreInfoUL);
    targetButton.parentElement.insertAdjacentHTML('beforeend', moreInfoDiv.outerHTML);
}

function searchVariety(resp){
    middlePart = document.querySelector('.topCenter');
    middlePart.innerHTML = "";
    var variety = resp.variety;
    var avg_rating = resp.average_rating;
    title = document.createElement('h1');
    title.innerHTML = variety + " (Average Rating: " + avg_rating + ")";
    middlePart.appendChild(title);
    br = document.createElement("br");
    hr = document.createElement("hr");
    middlePart.appendChild(br);
    middlePart.appendChild(br);
    var wines = resp.featured_wines;
    for (var i = 0; i < wines.length; i++){
        htmlEle = createSingleReviewHTML(wines[i]);
        middlePart.appendChild(htmlEle);
        middlePart.appendChild(br);
    }
    moreInfoButtons = document.querySelectorAll('.moreInfoButton');
    for (var i = 0; i < moreInfoButtons.length; i++){
        moreInfoButtons[i].addEventListener('click', this.BOTTLES_GET.bind(this));
    }
}

UID = -1

createNewUserButton1 = document.querySelector('.createNewUserButton1');
createNewUserButton1.addEventListener('click', this.openNewUserForm.bind(this))

createNewUserButton2 = document.querySelector('.createNewUserButton2');
createNewUserButton2.addEventListener('click', this.USERS_POST.bind(this))

signInButton = document.querySelector('.signIn');
signInButton.addEventListener('click', this.USERS_GET.bind(this))

// Link to delete user and sign out buttons
signOutButton = document.querySelector('.signOut');
signOutButton.addEventListener('click', this.signOut.bind(this))

deleteUserButton = document.querySelector('.deleteUser');
deleteUserButton.addEventListener('click', this.USERS_DELETE.bind(this));

createReviewButton = document.querySelector('.createReview');
createReviewButton.addEventListener('click', this.createReview.bind(this))

varietyButton = document.querySelector('.varietyButton');
varietyButton.addEventListener('click', this.REVIEWS_GET_VARIETY.bind(this))

