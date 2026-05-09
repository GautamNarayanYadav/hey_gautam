fetch('/api/main-page/')
.then(response => response.json())
.then(data => {

    document.getElementById("title").innerText =
        data.title;

    document.getElementById("subtitle").innerText =
        data.subtitle;

    document.getElementById("description").innerText =
        data.description;

    document.getElementById("about_title").innerText =
        data.about_title;

    document.getElementById("about_description").innerText =
        data.about_description;

    document.getElementById("projects").innerText =
        data.total_projects;

    document.getElementById("experience").innerText =
        data.years_experience;

    document.getElementById("clients").innerText =
        data.happy_clients;

    document.getElementById("profile_image").src =
        data.profile_image;

    document.getElementById("github_btn").href =
        data.github_url;

    document.getElementById("linkedin_btn").href =
        data.linkedin_url;

});