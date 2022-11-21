<template>
  <div>
    <div class="wrap">
      <!-- <div class="random-img"></div> -->
      <!-- <img src="@/assets/tumblr_mflsddIQER1rtrofoo1_500.gif" alt="" class="login-img"  id="movingPoster"> -->
      <!-- <img src="@/assets/23053C4758A511D106.gif" alt="" class="login-img"  id="movingPoster"> -->
      <!-- <img v-for="name in images" :key="name.id" :src="require(`@/assets/images${name}`)" alt="" class="login-img"  > -->
      <img id="movingPoster" border="0">
      <!-- class="login-img" -->
      <div class="form-wrap">
        <!-- <h1>LogIn Page</h1> -->
        <div class="container">
        <div class="button-wrap">
          <div id="btn"></div>
          <button type="button" class="togglebtn">Log in</button>
          <button type="button" class="togglebtn" @click="goToSignUp">회원가입</button>
        </div>
        <!-- <div class="container"> -->
          
          <form @submit.prevent="logIn" id="login" class="input-group">
            <!-- <label for="username">username : </label> -->
            <!-- <div class="container justify-content-center"> -->
            <input type="text"  class="input-field" placeholder="User name" required v-model="username"><br>
            <!-- </div> -->
            
            <!-- <label for="password"> password : </label> -->
            <input type="password" class="input-field" placeholder="Enter Password" required v-model="password">
           
            <div class="find-btn">
              <p><input type="checkbox" class="checkbox">Remember Password</p>
              <button class="submit" id="find-btn1">Login</button>
            </div>
          </form>
          </div>
      </div>
      <!-- <input type="submit" value="logIn"> -->
    <!-- </div> -->
    </div>
  </div>
</template>

<script>
// const images = [
//   'tumblr_mflsddIQER1rtrofoo1_500.gif', 'ySPeTDW.gif',
//   '02_Looper_(2012).gif', 'avengers-infinity-war-movie.gif',
//   '23053C4758A511D106.gif'
// ]
// const chosenImage = images[Math.floor(Math.random() * images.length)]
// const bgImage = document.createElement("img")
// bgImage.src = `@/assets/${chosenImage}`
// document.div.appendChild(bgImage)

// setInterval(() => {
//   let backgroundImg = document.getElementById('movingPoster')
//   let imgArr = ['@/assets/images/tumblr_mflsddIQER1rtrofoo1_500.gif',
// '@/assets/images/ySPeTDW.gif', '@/assets/images/02_Looper_(2012).gif', 
// '@/assets/images/avengers-infinity-war-movie.gif', '@/assets/images/23053C4758A511D106.gif'
// ]
//   console.log(backgroundImg)
//   let ranNum = Math.floor(Math.random() * imgArr.length)
//   console.log(imgArr[ranNum])
//   backgroundImg.src = imgArr[ranNum]
// },5000)

export default {
  name: 'LogInView',
  data() {
    return {
      username: null,
      password: null,
      // images: ['tumblr_mflsddIQER1rtrofoo1_500.gif', 'ySPeTDW.gif', '02_Looper_(2012).gif', 'avengers-infinity-war-movie.gif', '23053C4758A511D106.gif'],
    }
  },
  created() {
    this.changeImg()
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn', payload)
    },
    goToSignUp () {
      this.$router.push({ name: 'SignUpView'})
    },
    changeImg(){
      let imgArray = new Array()
      // imgArray[0] = "C:/Users/J/OneDrive/바탕 화면/final_pjt/Movie_Recommend/final-pjt-front/src/assets/tumblr_mflsddIQER1rtrofoo1_500.gif"
      imgArray[0] = "02_Looper_(2012).gif"
      // imgArray[1] = "C:/Users/J/OneDrive/바탕 화면/final_pjt/Movie_Recommend/final-pjt-front/src/assets/23053C4758A511D106.gif"
      // imgArray[1] = "C:/Users/J/OneDrive/바탕 화면/final_pjt/Movie_Recommend/final-pjt-front/src/assets/23053C4758A511D106.gif"
      // imgArray[2] = "C:/Users/J/OneDrive/바탕 화면/final_pjt/Movie_Recommend/final-pjt-front/src/assets/02_Looper_(2012).gif"
      // imgArray[2] = "C:/Users/J/OneDrive/바탕 화면/final_pjt/Movie_Recommend/final-pjt-front/src/assets/02_Looper_(2012).gif"
      // imgArray[3] = "C:/Users/J/OneDrive/바탕 화면/final_pjt/Movie_Recommend/final-pjt-front/src/assets/4.gif"
      // imgArray[3] = "C:/Users/J/OneDrive/바탕 화면/final_pjt/Movie_Recommend/final-pjt-front/src/assets/4.gif"

      let imgNum = Math.round(Math.random()*3)
      let objImg = document.getElementById('movingPoster')
      console.log(objImg)
      objImg.src = imgArray[imgNum]
      
      

      // let backgroundImg = document.getElementById('movingPoster')
      // let imgArr = ['@/assets/images/tumblr_mflsddIQER1rtrofoo1_500.gif',
      // '@/assets/images/ySPeTDW.gif', '@/assets/images/02_Looper_(2012).gif', 
      // '@/assets/images/avengers-infinity-war-movie.gif', '@/assets/images/23053C4758A511D106.gif'
      // ]
      // let ranNum = Math.floor(Math.random() * imgArr.length)
      // backgroundImg.src = imgArr[ranNum]
    }

  },
  


}
</script>
<style scoped>

.wrap {
    height: 100%;
    width: 100%;
    /* background-image: url(img/background.jpg); */
    background-position: center;
    background-size: cover;
    position: absolute;
}
.form-wrap {
    width: 380px;
    height: 400px;
    position: relative;
    margin: 15% auto;
    background: #fff;
    padding: 10px;
    overflow: hidden;
    opacity: 0.8;
    justify-content: center;
    align-items: center;
    animation: fadein 3s;
}
@keyframes fadein {
  from {
    opacity: -1;
  }
  to {
    opacity: 1;
  }
}
.button-wrap {
    width: 230px;
    margin: 10px auto;
    position: relative;
    box-shadow: 0 0 600px 9px #fcae8f;
    border-radius: 30px;
}
.togglebtn {
    padding: 10px 30px;
    cursor: pointer;
    background: transparent;
    border: 0;
    outline: none;
    position: relative;
}
#btn {
    top: 0;
    left: 0;
    position: absolute;
    width: 110px;
    height: 100%;
    background: linear-gradient(to right, #ff105f, #ffad06);
    border-radius: 30px;
    transition: .5s;
}
.social-icons {
    margin: 30px auto;
    text-align: center;
}
.social-icons img {
    width: 30px ;
    cursor: pointer;
}
.input-group {
    top: 50px;
    justify-content: center;
    align-items: center;
    position:relative;
    width: 300px;
    transition: .5s;
}
.input-field {
    width: 100%;
    padding: 10px 10px;
    margin: 0px  0px 1px -1px;
    border: none;
    border-bottom: 1px solid #999;
    outline: none;
    background: transparent;
}

.submit {
    /* left: 50px !important; */
    width: 65%;
    padding: 5px 30px 5px 30px; 
    cursor: pointer;
    display: block;
    /* margin: -10px 0px 10px 10px ; */
    margin: auto;
    background: linear-gradient(to right, #ff105f, #ffad06);
    border: 0;
    outline: none;
    border-radius: 30px;
}
.checkbox {
    margin: 15px 10px 20px -80px;
    /* margin: 40px 30px; */
}
/* .find-btn{
  text-align: center;
} */
#find-btn1 {
  display: inline-block;
  margin: 30px 0px 0px 120px;

}
span {
    color: #777;
    font-size: 12px;
    bottom: 68px;
    position: absolute;
}
#login {
    left: 20px;
    
}
#register {
    left: 450px;
}
.login-img{
  width: 600px;
  height: 800px;
  opacity: 0.5;
  position: absolute;
  top: 20%;
  left: 50%;
  z-index: -1;
  display: flex;
  justify-content: center;
  align-items: center;
  transform: translate(-50%, -20%);
  animation: fadeout 2s;

}
@keyframes fadeout {
  from {
    opacity: 1;
  }
  to {
    opacity: 1;
  }
}
</style>