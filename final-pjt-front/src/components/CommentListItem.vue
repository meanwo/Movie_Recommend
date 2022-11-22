<template>
 <div class=col-lg-8>

    <!-- Comments section-->
    <section class="mb-5">
      <div class="card bg-dark">
        <div class="card-body">
             <!-- Comment with nested comments-->
         <div class="d-flex mb-4">
            <!-- Parent comment-->
            <div class="flex-shrink-0"><img class="icon rounded-circle" src="@/assets/아이콘.png" alt="..." /></div>
            <div class="ms-3">

    <div v-if="comment.spoiler">
      <div class="text-light comment-box m-1">
      <!-- <div class="flex-shrink-0"><img src="@/assets/아이콘.png" alt="" class="rounded-circle"></div> -->
       <!-- <div class="ms-3"> -->
        <div class="fw-bold">{{comment.username}}</div>
      <div class="box">주의! 스포일러가 담긴 댓글입니다! <toggle-button @change="showComment()"/> <button @click="deleteComment">X</button></div>
      <!-- </div> -->
      
      <div v-if="checkSpoiler">
        <h5 class="text-light comment">{{comment.content}}</h5>
      </div>
     
    </div>  
    </div>

    <div v-else>
      <div class="text-light comment-box m-1">
        <!-- <div class="flex-shrink-0"><img src="@/assets/아이콘.png" alt="" class="icon rounded-circle"></div> -->
        <div class="ms-3">
      <!-- <div class=" text-light box"> -->
      <div class="fw-bold">{{comment.username}}</div>
      </div>  
      <h5 class="text-light comment">{{comment.content}} <button @click="deleteComment">X</button></h5>
     </div>
      </div>
      </div>
      </div>
    </div>
 

  </div>
  </section>
  
    <!-- <div class=" text-light box">
      <h4><img src="@/assets/아이콘.png" alt="" class="icon"> {{comment.username}}</h4>
    </div>  
      <p class="text-light">{{comment.content}}</p> -->
      <!-- <hr> -->
     
   
    <!-- border-box text- -->
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";

export default {
  name: "CommentListItem",
  data() {
    return {
      checkSpoiler: false,

    };
  },
  props: {
    comment: String,
  },
  methods: {
    deleteComment() {
      axios({
        method: "delete",
        url: `${API_URL}/api/v2/comments/${this.comment.id}`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          console.log(res)
          
          this.$emit('delete-comment', this.comment.id)
          // this.$emit('delete-comment', res.data)
        })
        .catch((err) => {
          console.log(err)
        })

    },
    showComment() {
      this.checkSpoiler = !this.checkSpoiler;
      return this.checkSpoiler;
    },
  },
};
</script>

<style scoped>
.card {
  position: relative;
  display: flex;
  flex-direction: column;
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0, 0, 0, 0.125);
  border-radius: 0.25rem;
}
.card-body {
  flex: 1 1 auto;
  padding: 1rem 1rem;
}
.big-box{
  /* width: 400px;
  height: 80px; */
  /* justify-content: center; */
  /* align-items: center; */
  
}
.box{
   /* display: flex; 
  flex-direction: row; 
  justify-content: start;
  float:left; */

  /* width: 300px;
  height: 25px; */
  /* justify-content: start; */
  /* align-items: start; */
  /* margin: 0px 0px 0px 100px; */
}
.comment-box{
  /* width: 700px;
  height: 100px; */
  /* margin: 10px 10px 0px 10px; */
  
  /* justify-content: center;
  align-items: center; */
}
/* .comment{
  display:flex;
  justify-content: start;
  width: 700px;
  height: 30px;
  text-align: start;
  word-break: keep-all;
} */
.icon{
  width: 30px;
  height: 30px;
}
.fw-bold {
  font-weight: 700 !important;
}
</style>