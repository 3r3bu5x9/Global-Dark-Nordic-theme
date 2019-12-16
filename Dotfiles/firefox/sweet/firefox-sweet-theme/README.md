![Screenshot of the theme](screenshot.png)

## Description

A dark and modern theme for firefox

This theme is supposed to work with current supported Firefox releases:

- Firefox 68.0
- Firefox 68 ESR
- Firefox 60 ESR
- Firefox 69.0 Beta
- Firefox 70.0 Nightly

***Firefox 60 ESR issues:***

*(Dark theme variant is broken in Firefox < 67).*

*https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme#Browser_compatibility*

## Installation

### Installation script
```sh
git clone https://github.com/EliverLara/firefox-sweet-theme/ && cd firefox-sweet-theme
./scripts/install.sh
```

#### Script options
- -f `<firefox_folder>` *optional*
	- Set custom Firefox folder path, for example `~/.mozilla/icecat/`.
	- Default: `~/.mozilla/firefox/`

- -p `<profile_folder>` *optional*
	- Set custom profile folder name, for example `e0j6yb0p.default-nightly`
	- Default: `*.default` (standard default profile)

- -g *optional*
	- Auto enable GNOMISH extra features `hide-single-tab.css` & `matching-autocomplete-width.css`


### Manual installation
1. Go to `about:support` in Firefox.

2. Application Basics > Profile Directory > Open Directory.

3. Open directory in a terminal.

4. Create a `chrome` directory if it doesn't exist.

	```sh
	mkdir -p chrome
	cd chrome
	```

5. Clone this repo to a subdirectory:

	```sh
	git clone https://github.com/EliverLara/firefox-sweet-theme.git
	```

6. Create single-line user CSS files if non-existent or empty (at least one line is needed for `sed`):

	```sh
	[[ -s userChrome.css ]] || echo >> userChrome.css
	```

7. Import this theme at the beginning of the CSS files (all `@import`s must come before any existing `@namespace` declarations):

	```sh
	sed -i '1s/^/@import "firefox-sweet-theme\/userChrome.css";\n/' userChrome.css
	```

8. Symlink preferences file:

	```sh
	ln -s chrome/firefox-sweet-theme/configuration/user.js ../user.js
	```

9. Restart Firefox.

10. Open Firefox customization panel and move the new tab button to headerbar.

11. Be happy with your new vibrant Firefox.


## Uninstalling

1. Go to your firefox profile folder. (Go to about:support in Firefox > Application Basics > Profile Directory > Open Directory)

2. Remove the `chrome` folder.


## Enabling optional features
Open `chrome/firefox-sweet-theme/userChrome.css` with a text editor and follow instructions to enable extra features. Keep in mind this file might change in future versions and your configuration will be lost. You can copy the @imports you want to enable to a new file named `customChrome.css` directly in your `chrome/firefox-sweet-theme` directory if you want it to survive updates. Remember all @imports must be at the top of the file, before other statements.

Alternatively you can run installation script with `-g` flag to auto install GNOMISH features.

```sh
./scripts/install.sh -g
```

*Those features are not included by default, because can introduce bugs or Firefox functionalities lost.*

- **hide-single-tab.css** *GNOMISH*

	Hide the tab bar when only one tab is open.

	You should move the new tab button somewhere else for this to work, because by default it is on the tab bar too.

- **matching-autocomplete-width.css** *GNOMISH*

	Limit the URL bar's autocompletion popup's width to the URL bar's width.

- **system-icons.css**

	Use system theme icons instead of Adwaita icons included by theme.

- **symbolic-tab-icons.css**

	Make all tab icons look kinda like symbolic icons.

## Known bugs

### CSD have sharp corners
See upstream [bug](https://bugzilla.mozilla.org/show_bug.cgi?id=1408360).

### Icons color broken with system-icons.css
Icons might appear black where they should be white on some systems. I have no idea why, but you can adjust them directly in the `system-icons.css` file, look for `--gnome-icons-hack-filter` & `--gnome-window-icons-hack-filter` vars and play with css filters.

## Development

If you wanna mess around the styles and change something, you might find these
things useful.

To use the Inspector to debug the UI, open the developer tools (F12) on any
page, go to options, check both of those:

- Enable browser chrome and add-on debugging toolboxes
- Enable remote debugging

Now you can close those tools and press Ctrl+Alt+Shift+I to Inspect the browser
UI.

Also you can inspect any GTK3 application, for example type this into a terminal
and it will run Epiphany with the GTK Inspector, so you can check the CSS styles
of its elements too.

```sh
GTK_DEBUG=interactive epiphany
```

Feel free to use any parts of my code to develop your own themes, I don't force
any specific license on your code.

## Credits
Based on the awesome [gnome theme](https://github.com/rafaelmardojai/firefox-gnome-theme) by **[Rafael Mardojai CM](https://github.com/rafaelmardojai)**
