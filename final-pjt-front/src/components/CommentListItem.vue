<template>
  <!-- d-flex flex-column -->
  <div class=" flex big-box">

    <div v-if="comment.spoiler">
      <div class="text-light box">
      <h4><img src="@/assets/아이콘.png" alt="" class="icon"> {{comment.username}}</h4>
      <div>주의! 스포일러가 담긴 댓글입니다! <toggle-button @change="showComment()"/> <button @click="deleteComment">X</button></div>
      
      
     
      <div v-if="checkSpoiler">
        <h5 class="text-light">{{comment.content}}</h5>
      </div>
    </div>  
    </div>

    <div v-else>
      <div class=" text-light box">
      <h4><img src="@/assets/아이콘.png" alt="" class="icon"> {{comment.username}}</h4>
    </div>  
      <h5 class="text-light">{{comment.content}}</h5>
      <button @click="deleteComment">X</button>
    </div>
  
  
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
    comment: Object,
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

<style>
.big-box{
  width: 400px;
  height: 80px;
  /* justify-content: center; */
  /* align-items: center; */
  
}
.box{
  float:left;

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
  
  justify-content: center;
  align-items: center;
}
.icon{
  width: 20px;
  height: 20px;
}
</style>