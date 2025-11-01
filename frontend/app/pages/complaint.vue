<script setup lang="ts">
import PowerMap from "~/components/PowerMap.vue";
import { ref } from "vue";

const name = ref("");
const phone = ref("");
const area = ref("");
const pincode = ref("");
const description = ref("");

</script >
 <template>
  <main>
    <div class="complaint-container">
      <h2 class="title">Report a Power Outage</h2>
      <form class="complaint-form" @submit.prevent="() => console.log('submitted')">
        <div class="form-group">
          <label for="name">Full Name</label>
          <input id="name" v-model="name" type="text" placeholder="Enter your name" required />
        </div>

        <div class="form-group">
          <label for="phone">Phone Number</label>
          <input id="phone" v-model="phone" type="tel" placeholder="Enter your phone number" required />
        </div>

        <div class="form-group">
          <label for="area">Area / Locality</label>
          <input id="area" v-model="area" type="text" placeholder="Enter your area or village name" required />
        </div>

        <div class="form-group">
          <label for="pincode">Pincode</label>
          <input id="pincode" v-model="pincode" type="text" placeholder="e.g. 560001" required />
        </div>

        <div class="form-group">
          <label for="description">Describe the Issue</label>
          <textarea
              id="description"
              v-model="description"
              rows="4"
              placeholder="Describe the power issue or duration of outage..."
          ></textarea>
        </div>

        <div class="form-group">
          <button type="submit" class="submit-btn">Submit Complaint</button>
        </div>
      </form>
    </div>
  </main>
</template>

<style scoped lang="scss">
main {
  height: 100vh;
  padding: 5%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.complaint-container {
  width: 100%;
  max-width: 600px;
  background-color: var(--color-surface-container-low);
  padding: var(--padding-lg);
  border-radius: var(--border-radius);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.title {
  text-align: center;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--color-on-surface);
}

.complaint-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.form-group {
  display: flex;
  flex-direction: column;

  label {
    margin-bottom: 0.5rem;
    font-weight: 500;
    color: var(--color-on-surface-variant);
  }

  input,
  textarea {
    background-color: var(--color-surface-container);
    border: 1px solid var(--color-outline-variant);
    border-radius: var(--border-radius-sm);
    padding: 0.75rem;
    color: var(--color-on-surface);
    font-size: 1rem;
    outline: none;
    transition: border-color 0.2s ease;

    &:focus {
      border-color: var(--color-primary);
    }
  }
}

.submit-btn {
  background-color: var(--color-primary);
  color: var(--color-on-primary);
  padding: 0.75rem 1rem;
  border: none;
  border-radius: var(--border-radius);
  font-weight: 600;
  cursor: pointer;
  transition: background-color 0.2s ease;

  &:hover {
    background-color: var(--color-primary-container);
  }
}
</style>
