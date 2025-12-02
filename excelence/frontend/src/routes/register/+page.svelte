<script lang="ts">
  import { goto } from '$app/navigation';
  import { registerUser } from '$lib/services/api';
  import { jwt_token } from '$lib/stores/auth';

  let email = '';
  let password = '';
  let error = '';
  let loading = false;

  async function handleSubmit() {
    error = '';
    if (password.length < 8) {
      error = 'Password must be at least 8 characters long.';
      return;
    }
    const passwordRegex = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    if (!passwordRegex.test(password)) {
      error = 'Password must contain at least one letter and one number.';
      return;
    }

    loading = true;
    try {
      const data = await registerUser(email, password);
      if (data.status === 'success' && data.data.token.access_token) {
        jwt_token.set(data.data.token.access_token);
        goto('/dashboard');
      } else {
        error = 'Registration successful, but no token received.';
      }
    } catch (e: any) {
      error = e.message || 'An unexpected error occurred.';
    } finally {
      loading = false;
    }
  }
</script>

<h1>Register</h1>
<form on:submit|preventDefault={handleSubmit}>
  <div>
    <label for="email">Email</label>
    <input id="email" type="email" bind:value={email} required />
  </div>
  <div>
    <label for="password">Password</label>
    <input id="password" type="password" bind:value={password} required />
  </div>
  {#if error}
    <p style="color: red;">{error}</p>
  {/if}
  <button type="submit" disabled={loading}>
    {#if loading}
      Registering...
    {:else}
      Register
    {/if}
  </button>
</form>