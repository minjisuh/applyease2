<script>
    import Flatpickr from 'svelte-flatpickr';
    import 'flatpickr/dist/flatpickr.css';
    import { format } from 'date-fns';

    let userInfo = {
        name: '',
        birth: '',
        phone: '',
        email: '',
        intro2: '',
        imageUrl: '',
        address: ''
    };

    let careers = [
        { startDate: null, endDate: null, company: '', department: '', isEditable: true },
    ];
    let educationHistory = [
        { degree: '', school: '', major: '', isEditable: true },
    ];

    function handleFileUpload(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = (e) => {
                userInfo.imageUrl = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    }

    let isEditing = false;

    function toggleEdit() {
        isEditing = !isEditing;
    }

    function addCareer() {
        careers = [...careers, { startDate: null, endDate: null, company: '', department: '', isEditable: true }];
    }

    function saveCareer(index) {
        careers[index].isEditable = false;
    }

    function formatDate(date) {
        return date ? format(new Date(date), 'yyyy.MM') : '';
    }



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
        const popup = window.open(`/userInfoPopup.html?data=${dataParam}`, 'UserInfoPopup', 'width=800,height=1500');
    }
</script>


<div class="container">
    <header class="page-header">
        <h1>📜 이력서</h1>
        <button on:click={openPopup}>미리보기</button>
    </header>



    <div class='basicinfo'>
        <div class='header'>
          <h2>😊 기본 정보</h2>
          <button on:click={toggleEdit}>{isEditing ? '📥' : '🔧'}</button>
        </div>
        <div class="container">
          <div class="photo-upload">
            <label for="file-upload">
              {#if userInfo.imageUrl}
                <img src={userInfo.imageUrl} alt="Uploaded Image" class="uploaded-image" />
              {:else}
                <img src="/empty.png" alt="Empty Square" class="uploaded-image" />
              {/if}
            </label>
            <input id="file-upload" type="file" accept="image/*" on:change={handleFileUpload} style="display: none;" />
          </div>
          <div class="user-info">
            <div>
              <input type="text" bind:value={userInfo.name} placeholder="이름" class="inputField" class:noBorder={!isEditing} disabled={!isEditing} />
            </div>
            <div> 
              <input type="text" bind:value={userInfo.birth} placeholder="생년월일 (YYYY/MM/DD)" class="inputField" class:noBorder={!isEditing} disabled={!isEditing} />
              <input type="text" bind:value={userInfo.phone} placeholder="전화 번호" class="inputField" class:noBorder={!isEditing} disabled={!isEditing} />
            </div>
            <div>
                <input type="email" bind:value={userInfo.email} placeholder="이메일" class="inputField" class:noBorder={!isEditing} disabled={!isEditing} />
                <input type="text" bind:value={userInfo.address} placeholder="주소" class="inputField" class:noBorder={!isEditing} disabled={!isEditing} />
            </div>
          </div>
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
        color: rgb(66, 66, 66);
        font-weight: bold;
    }

    button {
        padding: 2px 4px;
        margin-left: 10px;
        border: none;
        border-radius: 5px;
        background-color: rgb(209, 209, 209);
        font-size: 15px;
        cursor: pointer;
    }

    .basicinfo .container {
        display : flex;
        flex-direction : row;

    }

    .photo-upload {
        flex: 0 0 auto;
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-right : 20px;
    }

    .uploaded-image {
        width: 3cm;
        height: 4cm;
        margin-top: 10px;
        cursor: pointer;
        margin-right : 20px;
    }

    .user-info {
        flex: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        }

    .inputField {
        border: 1px solid #ccc; /* 기본 테두리 */
        width : 400px;
        height : 20px;
        padding: 5px;
        margin-bottom: 5px;
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

    .intro .inputField {
        margin-left : 20px;
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
  
