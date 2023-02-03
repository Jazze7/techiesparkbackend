// Events data array
events_data = [
    {
        id: 1,
        title: "Business meeting organised on the 28th August at Kannur",
        date: "Aug. 25, 2022",
        description:
            "As part of Talrop's Invest in Kerala campaign, a business meeting was organised on 28th August at Kannur.The event was held at Talrop's Techies Park, NAHER Arts and Science College, Kanhirode, Kannur and many potential Angel Investors took part in the meeting. Talked about the needs and opportunities of Angel Investors in a startup and the risks & benefits of Angel Investing were also discussed. A descriptioned overview of Talrop's mission and investment opportunities in Talrop's startups were discussed.",
        image: "../static/assets/images/safeer.png",
        number: "../static/assets/images/01.png",
    },
    {
        id: 2,
        title: "MLA Mr. Sunny Joseph visited Talrop's recently established Techies Park on NAHER Arts and Science College",
        date: "Aug. 25, 2022",
        description:
            "Talrop's Techies Park at the NAHER Arts & Science College under KMJ Management were visited by MLA Mr. Sunny Joseph, Peravoor Assembly Constituency in Kannur District.In order to strengthen Kerala's startup ecosystem, he also pledged his complete support for Talrop's initiatives in the Peravoor Assembly Constituency, including the implementation of Techies Park.",
        image: "../static/assets/images/mla.png",
        number: "../static/assets/images/02.png",
    },
    {
        id: 3,
        title: "The Inspector of Police Mr Sibeesh VP of Kannur Chakkarakal station, inaugurated the Cyber Month programs",
        date: "Aug. 25, 2022",
        description:
            "Cyber Month program at Talrop's new Techies Park at NAHER Arts and Science College campus of Kannur Assembly Constituency was inaugurated by the Inspector of Police, Mr Sibeesh VP of Chakkarakal station, Kannur.As part of Cyber Month, a lot of free programs suitable for every group of people are organised at Techies Park. Community development is an important aspect that Talrop focuses on, as part of developing a strong startup ecosystem in Kerala. Through Cyber Month programs, Talrop hopes to bring the people from every assembly constituency to Talrop's system and to grow as a community.",
        image: "../static/assets/images/police.png",
        number: "../static/assets/images/3.png",
    },
];

// Rendering into html
events_data.map((event) => {
    html = ` <li>
    <div class="left">
      <h2>${event.title}</h2>
      <small>${event.date}</small>
      <p>${event.description.slice(0, 300)}...</p>
      <div class="bottom">
        <button>
            <span class="button-name"> View More </span>
            <img src="../static/assets/images/arrow.png" alt="arrow_image" />
        </button>
        <div class="event-number">
                <img src=${event.number} alt="count" />
        </div>
      </div>
    </div>
    <div class="right">
        <div class="ImageContainer">
            <img src=${event.image} alt="event image" />
        </div>
    </div>
    </li>
`;
    $(".cards").append(html);
});

// active the navbar
let navbar = $("#home header .right ul li a");
console.log(navbar);
$(document).ready(function () {
    $(navbar).click(function () {
        $(navbar).removeClass("active");
        $(this).addClass("active");
    });
});

// screen scrolling active
window.onscroll = function () {
    let scrollY = window.pageYOffset;
    let sections = $("section");
    sections.map((index, section) => {
        const sectionHeight = section.clientHeight;
        const sectionTop = section.getBoundingClientRect().top + scrollY - 50;
        const sectionId = section.getAttribute("id");
        if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
            $(navbar).removeClass("active");
            $("#home header .right ul li a[href*=" + sectionId + "]").addClass(
                "active"
            );
        } else {
            $("#nav li a[href*=" + sectionId + "]").removeClass("active");
        }
    });
};

// hamburger button
$(document).ready(function () {
    $(".hamburger").click(function () {
        $(".menu").show();
        $(".menu ul").slideToggle("slow");
    });
    $(".menu").click(function () {
        $(".menu").hide();
    });
});

// video playing
let play_button = $(
    "section#home section#spotlight div.right div.button-container"
);
let video = $("section#home section#spotlight  div.video-player ");
let close = $("section#home section#spotlight div.video-player span");
let video_tag = $("section#home section#spotlight  div.video-player video");
let play_button2 = $("section#home section#spotlight div.left button");
$(play_button, play_button2).click(function () {
    $(video).show();
    $("body").css("overflow", "hidden");
});
$(close).click(function () {
    $(video).hide();
    if ($(video).hide()) {
        $("body").css("overflow", "scroll");
    }
});

// showing the password field
$("#login div.right form div.password div.eye-open").click(function () {
    $("form .password .eye-open").hide();
    $("form .password .eye-hide").show();
    $(" form .password input").attr("type", "text");
});
$("#login div.right form div.password div.eye-hide").click(function () {
    $("form .password .eye-hide").hide();
    $("form .password .eye-open").show();
    $(" form .password input").attr("type", "password");
});
