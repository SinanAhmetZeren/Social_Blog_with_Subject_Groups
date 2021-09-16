'use strict';


// SELECT ALL SUBJECT CONTAINERS, ADD EVENT LISTENERS
// AND DIRECT TO RELATED SUBJECT'S ARTICLES ON CLICK 
let allsubjects = document.getElementById("all-subjects-container");
const goToSubjectArticles = function (e) {
    const clickedSubjectID = e.target.closest('.single-subject-card');
    window.location = window.location.origin + `/subjects/subjectArticles/${clickedSubjectID.dataset.subject_id}`;
}
console.log("allsubjects:", allsubjects);
if (allsubjects)  allsubjects.addEventListener("click", goToSubjectArticles)

// SELECT ALL ARTICLE CONTAINERS, ADD EVENT LISTENERS
// AND DIRECT TO RELATED ARTICLE DETAIL PAGE ON CLICK 
let allarticles = document.getElementById("subject-articles-container");
const goToArticleDetail = function (e) {
    const clickedArticleID = e.target.closest('.single-article-card');
    console.log(window.location.origin + `/articles/detail/${clickedArticleID.dataset.article_id}`);
    window.location = window.location.origin + `/articles/detail/${clickedArticleID.dataset.article_id}`;
}
console.log("allarticles", allarticles);
if(allarticles) allarticles.addEventListener("click", goToArticleDetail)


// SELECT ALL PROFILE CONTAINERS, ADD EVENT LISTENERS
// AND DIRECT TO RELATED PROFILE ARTICLES PAGE ON CLICK 
let allprofiles = document.getElementById("allusers-profile-container");
const goToProfileArticles = function (e) {
    const clickedProfileID = e.target.closest('.allusers-profile');
    console.log(clickedProfileID);
    window.location = window.location.origin + `/accounts/public_profile/${clickedProfileID.dataset.username}`;
}
if(allprofiles) allprofiles.addEventListener("click", goToProfileArticles)



///////////////////////////////
// 1. select subject id from URL
let subjectID = window.location.pathname.split("/")[3];
// 3. find option with related id (value = id)
let options = document.querySelectorAll("option")
options.forEach(option => {
    console.log(option);
    if (option.value == subjectID) option.setAttribute("selected", "") 
})
