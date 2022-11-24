<template>
  <div class="col-lg-8 comment-item">
    <section class="mb-1">
      <div class="card bg-dark">
        <div class="card-body comment-box">
          <div v-if="comment.spoiler">
            <div class="text-light m-1">
              <div class="ms-3">
                <div class="fw-bold">
                  <img
                    class="icon rounded-circle"
                    src="@/assets/아이콘.png"
                    alt="..."
                  />{{ comment.username }}
                </div>
                <div>
                  <div v-if="!checkSpoiler" class="comment-content">
                    주의! 스포일러가 담긴 댓글입니다!
                  </div>
                  <toggle-button @change="showComment()" />
                  <button @click="deleteComment">X</button>
                </div>
                <div v-if="checkSpoiler">
                  <h5 class="text-light comment-content">
                    {{ comment.content }}
                  </h5>
                </div>
              </div>
            </div>
          </div>

          <div v-else>
            <div class="text-light m-1">
              <div class="ms-3">
                <div class="fw-bold">
                  <img
                    class="icon rounded-circle"
                    src="@/assets/아이콘.png"
                    alt="..."
                  />{{ comment.username }}
                </div>
              </div>
              <h5 class="text-light comment-content">
                {{ comment.content }} <button @click="deleteComment">X</button>
              </h5>
            </div>
          </div>
        </div>
      </div>
    </section>
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
          console.log(res);

          this.$emit("delete-comment", this.comment.id);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    showComment() {
      this.checkSpoiler = !this.checkSpoiler;
      return this.checkSpoiler;
    },
  },
};
</script>

<style scoped>
.comment-item {
  display: block;
  /* flex-direction: row; */
  /* justify-content: end; */
  /* margin: 0px 0px 0px 100px; */
  margin: 0 auto;
  width: 100%;
}
.card {
  /* width: 56%;
  margin: 0 auto; */
  position: relative;
  display: float;
  /* flex-direction: column; */
  min-width: 0;
  word-wrap: break-word;
  background-color: #fff;
  background-clip: border-box;
  border: 1px solid rgba(0, 0, 0, 0.125);
  border-radius: 0.25rem;
}
.card-body {
  /* flex: 1 1 auto; */
  /* padding: 1rem 1rem; */
  display: block;
}

.comment-box {
  display: block;
}

.icon {
  width: 30px;
  height: 30px;
  margin: 0px 5px 4px 0px;
}
.fw-bold {
  font-weight: 700 !important;
  text-align: start;
}
.comment-content {
  text-align: start;
}
</style>
