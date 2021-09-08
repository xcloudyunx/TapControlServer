import React from "react";

// import colors from "../config/colors";
// import constants from "../config/constants";

import Button from "./Button";

export default function IconButtonSettings(props) {
	return (
		<div style={styles.container}>
			<Button
				value="&#10005;"
				style={styles.button}
				onClick={props.onClick}
			/>
			{props.className}
			{props.id}
		</div>
	);
}

const styles = {
	button: {
		// width: "10%",
	}, container: {
		flex: 5,
	},
};