<script>
    export let userInfo = {};
    
    // Check if running inside a popup and retrieve userInfo from the window object
    if (typeof window !== 'undefined' && window.opener) {
      userInfo = window.opener.userInfo || {};
    }
  </script>
  
  <div>
    <h1>User Info:</h1>
    <p>Name: {userInfo.name}</p>
    <p>Email: {userInfo.email}</p>
    <!-- Add more fields as needed -->
  </div>
  