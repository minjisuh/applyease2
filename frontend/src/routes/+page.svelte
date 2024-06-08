<script>
</script>

<div class="app-container">
    <main>
        <slot></slot>
        <div class="animation-container">
            <div class="tape">
              <span class="word font1">APPLYEASE</span>
              <span class="word font2">APPLYEASE</span>
              <span class="word font3">APPLYEASE</span>
              <span class="word font4">APPLYEASE</span>
              <span class="word font5">APPLYEASE</span>
              <span class="word font6">APPLYEASE</span>
              <span class="word font7">APPLYEASE</span>
              <span class="word font8">APPLYEASE</span>
              <span class="word font9">APPLYEASE</span>
              <span class="word font10">APPLYEASE</span>
              <span class="word font1">APPLYEASE</span>
              <span class="word font2">APPLYEASE</span>
              <span class="word font3">APPLYEASE</span>
              <span class="word font4">APPLYEASE</span>
              <span class="word font5">APPLYEASE</span>
              <span class="word font6">APPLYEASE</span>
              <span class="word font7">APPLYEASE</span>
              <span class="word font8">APPLYEASE</span>
              <span class="word font9">APPLYEASE</span>
              <span class="word font10">APPLYEASE</span>
              <span class="word font1">APPLYEASE</span>
              <span class="word font2">APPLYEASE</span>
              <span class="word font3">APPLYEASE</span>
              <span class="word font4">APPLYEASE</span>
              <span class="word font5">APPLYEASE</span>
              <span class="word font6">APPLYEASE</span>
              <span class="word font7">APPLYEASE</span>
              <span class="word font8">APPLYEASE</span>
              <span class="word font9">APPLYEASE</span>
              <span class="word font10">APPLYEASE</span>
              <span class="word font1">APPLYEASE</span>
              <span class="word font2">APPLYEASE</span>
              <span class="word font3">APPLYEASE</span>
              <span class="word font4">APPLYEASE</span>
              <span class="word font5">APPLYEASE</span>
              <span class="word font6">APPLYEASE</span>
              <span class="word font7">APPLYEASE</span>
              <span class="word font8">APPLYEASE</span>
              <span class="word font9">APPLYEASE</span>
              <span class="word font10">APPLYEASE</span>
              <span class="word font1">APPLYEASE</span>
              <span class="word font2">APPLYEASE</span>
              <span class="word font3">APPLYEASE</span>
              <span class="word font4">APPLYEASE</span>
              <span class="word font5">APPLYEASE</span>
              <span class="word font6">APPLYEASE</span>
              <span class="word font7">APPLYEASE</span>
              <span class="word font8">APPLYEASE</span>
              <span class="word font9">APPLYEASE</span>
              <span class="word font10">APPLYEASE</span>
              <span class="word font1">APPLYEASE</span>
              <span class="word font2">APPLYEASE</span>
              <span class="word font3">APPLYEASE</span>
              <span class="word font4">APPLYEASE</span>
              <span class="word font5">APPLYEASE</span>
              <span class="word font6">APPLYEASE</span>
              <span class="word font7">APPLYEASE</span>
              <span class="word font8">APPLYEASE</span>
              <span class="word font9">APPLYEASE</span>
              <span class="word font10">APPLYEASE</span>
              <span class="word font1">APPLYEASE</span>
              <span class="word font2">APPLYEASE</span>
              <span class="word font3">APPLYEASE</span>
              <span class="word font4">APPLYEASE</span>
              <span class="word font5">APPLYEASE</span>
              <span class="word font6">APPLYEASE</span>
            </div>

        
          </div>
        <div class="navigation">
            <h6>✖</h6>
            <h2 class = "word font3">Explore our site</h2>
            <ul>
              <li>
                <a href="/Home" class="folder-link">Home</a>
                <p class="description">채용 일정을 정리할 수 있습니다. </p>
              </li>
              <li>
                <a href="/Resume" class="folder-link">Resume</a>
                <p class="description">이력서 내용을 입력하고, 이력서 서식에 맞게 다운받을 수 있습니다.</p>
              </li>
              <li>
                <a href="/CoverLetter" class="folder-link">Cover Letter</a>
                <p class="description">자기소개서를 관리할 수 있습니다. </p>
              </li>
            </ul>
          </div>
        
        
    </main>

</div>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Anton&family=Jersey+10&family=Quicksand:wght@300..700&family=Tiny5&family=Zen+Dots&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Oswald&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Merriweather&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Raleway&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Open+Sans&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Sansita+Swashed&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Ubuntu&display=swap');
  
    .animation-container {
      overflow: hidden;
      width: 100%;
      white-space: nowrap;
    }
  
    .tape {
      display: inline-block;
      animation: moveTape 80s linear infinite;
    }
  
    .word {
      margin-top : 20px;
      font-size: 30px;
      margin-bottom : 50px;
      display: inline-block;
      padding-right: 20px; /* Add space between words */
    }
  
    @keyframes moveTape {
      0% {
        transform: translateX(0%);
      }
      100% {
        transform: translateX(-100%);
      }
    }
  
    .font1 {
      font-family: 'Jersey 10', sans-serif;
    }
    .font2 {
      font-family: 'Tiny5', cursive;
    }
    .font3 {
      font-family: 'Zen Dots', cursive;
    }
    .font4 {
      font-family: 'Quicksand', sans-serif;
    }
    .font5 {
      font-family: 'Merriweather', serif;
    }
    .font6 {
      font-family: 'Raleway', sans-serif;
    }
    .font7 {
      font-family: 'Open Sans', sans-serif;
    }
    .font8 {
      font-family: 'Anton', sans-serif;
    }
    .font9 {
      font-family: 'Sansita Swashed', cursive;
    }
    .font10 {
      font-family: 'Ubuntu', sans-serif;
    }


    .navigation {
    font-family: Arial, sans-serif;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;

    border : 1px solid #2a2c33;
    background-color: #aeb5bd;
  }

  .navigation h2 {
    color : rgb(37, 37, 37);
    border : 1px solid #ddd;
    text-align: center;
    margin-bottom: 20px;
    font-size : 30px;
  }
  .navigation h6 {
    text-align : right;
    margin : 0px;
    font-size : 30px;
  }

  .navigation ul {
    list-style-type: none;
    padding: 0;
  }

  .navigation li {
    display: flex;
    align-items: center;
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 20px;
    background-color: #fff;
  }


  .folder-link {
    display: block;
    width: 150px;
    font-size: 1.2rem;
    font-weight: bold;
    margin-left : 30px;
    color: #2b2929;
    
  }

  .description {
    margin-left: 20px;
    font-size: 1rem;
    color: #666;
  }

  .folder-link:hover {
    text-decoration: underline;
  }
  </style>