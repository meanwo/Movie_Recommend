<template>
  <div>
    <CommentListItem
      v-for="(comment, index) in comments"
      :key="index"
      :comment="comment"
    />
  </div>
</template>

<script>
import CommentListItem from '@/components/CommentListItem'
// import axios from "axios";

// const API_URL = "http://127.0.0.1:8000";
export default {
    name: 'CommentList',
    components: {
      CommentListItem,
    },
    props: {
      movieCard: Object,
      comments: Object,
    },

    methods: {
  
    },
    // created() { 
    //   this.getComments()
    // },
    // methods: {
    //   getComments() { 
    //     axios({
    //       method: 'get',
    //       url: `${API_URL}/api/v2/comments/list/${this.movieCard.id}/`
    //     })
    //       .then((res) => {
    //         console.log(res) 
    //         // this.comments = res.data;
    //         // console.log(this.comments)
    //       })
    //   }
    // }

};
</script>

<style></style>
