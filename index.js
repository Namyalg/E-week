var firebaseConfig = {
        apiKey: "AIzaSyB7b2iVuj62asIf_PU9vhLjLRHpDCH4sFc",
        authDomain: "e-week.firebaseapp.com",
        databaseURL: "https://e-week.firebaseio.com",
        projectId: "e-week",
        storageBucket: "e-week.appspot.com",
        messagingSenderId: "81995282172",
        appId: "1:81995282172:web:7ef4322f9ae04802a90979"
      };

firebase.initializeApp(firebaseConfig);
var database = firebase.database();
var firebaseOrdersCollection = database.ref().child('Questions');

function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}
function addques() {
    var d = new Date();
    var n = d.getTime();
    var question = document.getElementById("msg").value;
    document.getElementById("msg").value = "";
    firebaseOrdersCollection.child(n).set(question);

};


