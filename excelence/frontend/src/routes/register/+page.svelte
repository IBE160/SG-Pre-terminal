<script>
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

    loading = true;
    try {
      const response = await fetch('/api/v1/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, password }),
      });

      if (response.ok) {
        const data = await response.json();
        if (data.status === 'success' && data.data.access_token) {
          localStorage.setItem('jwt_token', data.data.access_token);
          window.location.href = '/dashboard';
        } else {
          error = 'Registration successful, but no token received.';
        }
      } else {
        const err = await response.json();
        error = err.detail || 'Registration failed';
      }
    } catch (e) {
      error = 'An unexpected error occurred.';
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