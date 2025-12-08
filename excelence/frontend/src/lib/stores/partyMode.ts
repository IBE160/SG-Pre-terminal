import { writable } from 'svelte/store';
import { browser } from '$app/environment';

function createPartyModeStore() {
    // Get initial party mode state from localStorage or default to false
    const getInitialState = (): boolean => {
        if (!browser) return false;
        const stored = localStorage.getItem('partyMode');
        return stored === 'true';
    };

    const { subscribe, set, update } = writable<boolean>(getInitialState());

    return {
        subscribe,
        toggle: () => {
            update(current => {
                const newValue = !current;
                if (browser) {
                    localStorage.setItem('partyMode', String(newValue));
                }
                return newValue;
            });
        },
        set: (value: boolean) => {
            if (browser) {
                localStorage.setItem('partyMode', String(value));
            }
            set(value);
        }
    };
}

export const partyModeStore = createPartyModeStore();

// Store for triggering animations
export const animationTrigger = writable<'confetti' | 'money' | null>(null);
