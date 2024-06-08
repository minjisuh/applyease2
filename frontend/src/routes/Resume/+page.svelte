<script>
    import Flatpickr from 'svelte-flatpickr';
    import 'flatpickr/dist/flatpickr.css';
    import { format } from 'date-fns';

    let userInfo = {
        name: '',
        phone: '',
        email: '',
        intro2 : ''
    };

    let isEditing = false;

    function toggleEdit() {
        isEditing = !isEditing;
    }

    let careers = [
        { startDate: null, endDate: null, company: '', department: '', isEditable: true },
    ];

    function addCareer() {
        careers = [...careers, { startDate: null, endDate: null, company: '', department: '', isEditable: true }];
    }

    function saveCareer(index) {
        careers[index].isEditable = false;
    }

    function formatDate(date) {
        return date ? format(new Date(date), 'yyyy.MM') : '';
    }

    let educationHistory = [];

    function addEducation() {
        educationHistory = [...educationHistory, { degree: '', school: '', major: '', isEditable: true }];
    }

    function editEducation(index) {
        educationHistory[index].isEditable = true;
        educationHistory = [...educationHistory];
    }

    function saveEducation(index) {
        educationHistory[index].isEditable = false;
        educationHistory = [...educationHistory];
    }

    function openPopup() {
        const data = {
            userInfo,
            careers,
            educationHistory
        };

        const dataParam = encodeURIComponent(JSON.stringify(data));
        const popup = window.open(`/userInfoPopup.html?data=${dataParam}`, 'UserInfoPopup', 'width=600,height=400');
    }



    



</script>

<div class="container">
    <header class="page-header">
        <h1>📜 이력서</h1>
        <button on:click={openPopup}>Open User Info Popup</button>
    </header>



    <div class = 'basicinfo'>
        <div class='header'>
            <h2>😊 기본 정보</h2>
            <button on:click={toggleEdit}>{isEditing ? '📥' : '🔧'}</button>
        </div>
        <div>
            <input type="text" bind:value={userInfo.name} placeholder="이름" class="inputField" class:noBorder={!isEditing} disabled={!isEditing} />
        </div>
        <div>
            <input type="text" bind:value={userInfo.phone} placeholder="전화 번호" class="inputField" class:noBorder={!isEditing} disabled={!isEditing} />
        </div>
        <div>
            <input type="email" bind:value={userInfo.email} placeholder="이메일" class="inputField" class:noBorder={!isEditing} disabled={!isEditing} />
        </div>
    </div>
      
    <div class="intro">
        <div class="header">
          <h2>📢 간단 소개</h2>
          <button on:click={toggleEdit}>{isEditing ? '📥' : '🔧'}</button>
        </div>
        <div>
            <textarea bind:value={userInfo.intro2} class="inputField" class:noBorder={!isEditing} disabled={!isEditing}></textarea>
        </div>
    </div>
      

    <div class='careers'>
        <div class='careerheader'>
            <h2>💼 경력</h2>
            <button on:click={addCareer}>+ 경력 추가</button>
        </div>
        {#each careers as career, index}
        <div class="career-input">
            {#if career.isEditable}
                <div class="time">
                    <Flatpickr bind:value={career.startDate} placeholder='입사 년도' options={{ dateFormat: "Y-m-d" }} />
                    <Flatpickr bind:value={career.endDate} placeholder='퇴사 년도' options={{ dateFormat: "Y-m-d" }} />
                </div>
                <input type="text" placeholder="회사명" bind:value={career.company} />
                <input type="text" placeholder="부서명/직책" bind:value={career.department} />
                <button on:click={() => saveCareer(index)}>저장</button>
            {:else}
                <div class="career-wrapper">
                    {formatDate(career.startDate)} - {formatDate(career.endDate)} / {career.company} / {career.department}
                </div>
            {/if}
        </div>
        {/each}
    </div>


    <div class='education'>
        <div class = 'educationheader'>
            <h2>🎓 학력</h2>
            <button on:click={addEducation}>+ 학력 추가</button>
        </div>
        {#each educationHistory as education, index}
            <div class="education-input">
                {#if education.isEditable}
                        <!-- 편집 가능한 입력 필드 -->
                    <select bind:value={education.degree}>
                        <option value="">학위 선택</option>
                        <option>학사</option>
                        <option>석사</option>
                        <option>박사</option>
                    </select>
                    <input type="text" placeholder="학교명" bind:value={education.school} />
                    <input type="text" placeholder="전공" bind:value={education.major} />
                    <button on:click={() => saveEducation(index)}>저장</button>
                {:else}
                    <!-- 편집 불가능한 텍스트로 표시 -->
                    <div>
                        {education.degree} | {education.school}대학교 | {education.major}전공
                        <button on:click={() => editEducation(index)}>수정</button>
                    </div>
                {/if}
            </div>
        {/each}
    </div>
    

</div>
  
  <style>
    .intro .inputField {
        width: 100%;
        height: 100px;
    }
    .container {
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin: 0 auto;
      padding: 20px;
      max-width: 1200px; /* 최대 너비를 설정하여 양 옆에 공간을 만듭니다 */
    }
  
    .page-header {
        width: 100%;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 70px;
        border-bottom : 0.5px solid gray;
    }
  
      
    h1 {
      margin-bottom : 5px;
      font-size: 30px;
      font-weight: bolder;
    }
  
    .page-header button {
        border: none;
        background-color: rgb(255, 255, 255);
        color: rgb(104, 104, 104);
        font-size: 15px;
        cursor: pointer;
    }

    .page-header button:hover {
    border-radius: 10px;
    padding : 10px;
    background-color: #7899a7;
    color: #fff;
    }


    .basicinfo {
        width: 100%;
        margin-bottom: 50px;
    }
    .basicinfo .header {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
        
    }

    h2 {
        margin: 0;
        font-size: 20px;
        color : rgb(66, 66, 66);
        font-weight:bold;
    }
    .basicinfo button {
        padding : 2px 4px;
        margin-left : 10px;
        border : none;
        border-radius : 5px;
        background-color: rgb(209, 209, 209);
        font-size: 15px;
        cursor: pointer;
    }
    .intro button {
        padding : 2px 4px;
        margin-left : 10px;
        border : none;
        border-radius : 5px;
        background-color: rgb(226, 226, 226);
        font-size: 15px;
        cursor: pointer;
    }

    
    .inputField {
        border: 1px solid #ccc; /* 기본 테두리 */
        padding: 5px;
        margin-bottom : 5px;
    }
    
    .inputField.noBorder {
        border: 2px solid #dfdfdf; /* 테두리 제거 */
        padding: 10px;
        background-color: white;
        border-radius: 5px;
    }

    .intro {
        width: 100%;
        margin-bottom: 50px;
    }
    .intro .header {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }
    

    .careers {
        width: 100%;
        margin-bottom: 50px;
    }
    .careers .careerheader {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }
    .careers .careerheader button{
        padding : 2px 4px;
        margin-left : 10px;
        border : none;
        border-radius : 5px;
        background-color: rgb(226, 226, 226);
        font-size: 15px;
        cursor: pointer;
    }
    
    .careers .career-input {
        margin-bottom: 20px;
    }
    .careers .career-input .career-wrapper{
        border: 2px solid #dfdfdf;
        padding: 20px;
        border-radius: 15px;
        font-weight: bold;
        color : rgb(90, 90, 90);
    }

    .careers .career-input input {
        margin-bottom: 10px;
        width : 550px;
        padding: 5px;
        font-size : 18px;
        border: 1px solid #dfdfdf;
        border-radius: 5px;
    }
    .careers .career-input .time {
        margin-bottom: 10px;
        margin-right : 5px;
    }
    .careers .career-input button {
        padding : 2px 4px;
        margin-left : 10px;
        border : none;
        border-radius : 5px;
        background-color: rgb(226, 226, 226);
        font-size: 15px;
        cursor: pointer;
    }

    
    .education {
        width: 100%;
        margin-bottom: 50px;
    }

    .education .educationheader {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }
    .education .educationheader button{
        padding : 2px 4px;
        margin-left : 10px;
        border : none;
        border-radius : 5px;
        background-color: rgb(226, 226, 226);
        font-size: 15px;
        cursor: pointer;
    }



    

    .education button {
        padding : 2px 4px;
        margin-left : 10px;
        margin-bottom : 5px;
        border : none;
        border-radius : 5px;
        background-color: rgb(226, 226, 226);
        font-size: 15px;
        cursor: pointer;
    }




  </style>
  
