<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Sean Ashley LinkedIn][linkedin-shield]][https://www.linkedin.com/in/sean-ashley/]
[![Joseph Lamonica LinkedIn][linkedin-shield]][https://www.linkedin.com/in/shivam-sh/]
[![Shivam Sharma LinkedIn][linkedin-shield]][https://www.linkedin.com/in/giuseppelamonica/]
[![Nicholas Palmar LinkedIn][linkedin-shield]][https://www.linkedin.com/in/nicolas-palmar/]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">SIZR Backend</h3>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
This is the backend of the SIZR project, working to store users in the database and generate shoe recommendations

### Built With

* [CockroachDB](https://www.cockroachlabs.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Pandas](https://pandas.pydata.org/)
* [SQLAlchemy](https://www.sqlalchemy.org/)



<!-- GETTING STARTED -->
## Getting Started

To use the app you need to interact with one of the endpoints at https://sizr-backend.azurewebsites.net/



<!-- USAGE EXAMPLES -->
## Usage

To use the backend, you can interact with the endpoints on postman.

Here is how to use each one.

### "/adduser", methods = ["POST"]
ENTER https://sizr-backend.azurewebsites.net/adduser in Postman
Make sure method is set to post.
Go to raw, and make sure it is set to JSON.

In the body, pass a JSON object looking something like this
```
    {
    "username" : "seanashley",
    "length" : 28.5,
    "width"  : 10.5,
    "gender" : "m",
    "like_bigger_fitting_shoes" : true,
    "like_smaller_fitting_shoes" : false,
    "min_price" : 50,
    "max_price" : 150
 }
```
Send the postman request and it should return the user, showing that this has succeeded



### '/recommendshoes', methods = ["POST"]
ENTER https://sizr-backend.azurewebsites.net/recommendshoes in Postman
Make sure method is set to post.
Go to raw, and make sure it is set to JSON.

In the body, pass a JSON object looking something like this
```
    {
    "username" : "seanashley"
    }
 ```

The backend will then return a json looking something like this for example, with the top recommended shoes and sizes
```
{"index":{"0":11,"1":15,"2":18},"name":{"0":"DON Issue 1","1":"Mamba Focus","2":"Harden
Stepback"},"brand":{"0":"Adidas","1":"Nike
","2":"Adidas"},"price":{"0":99.99,"1":99.99,"2":79.99},"size_shift":{"0":0.5,"1":0.5,"2":0.5},"picture":{"0":"pictures\/don-issue-1.png","1":"pictures\/mamba-focus.png","2":"pictures\/adidas-Harden-Stepback.jpeg"},"US
Size":{"0":8.0,"1":8.0,"2":8.0}}
```



<!-- LICENSE -->
## License

Distributed under the Apache License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Sean Ashley - sean.d.ashley@gmail.com
Joseph Lamonica - g.lamonica02@gmail.com
Nicolas Palmar - nicolas.palmar8@gmail.com
Shivam Sharma - shivam.sharm@icloud.com










<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/github_username
