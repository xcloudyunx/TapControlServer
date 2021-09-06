import React from "react";

import colors from "../config/colors";
import constants from "../config/constants";

export default function Button(props) {
	return (
		<div style={Object.assign([], props.style, styles.container)}>
			<button
				style={styles.button}
				onClick={props.onClick}
			>
				{props.value}
			</button>
		</div>
	);
}

const styles = {
	button: {
		flex: 1,
		backgroundColor: colors.white,
		color: colors.black,
		fontWeight: "bold",
		borderRadius: constants.buttonRadius,
		display: "flex",
		justifyContent: "center",
		alignItems: "center",
	},
	container: {
		display: "flex",
	}
};