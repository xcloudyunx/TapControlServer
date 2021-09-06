import React from "react";

import colors from "../config/colors";
import constants from "../config/constants";

export default function IconButton(props) {
	return (
		<div style={{
			width: props.size,
			height: props.size,
			display: "flex",
		}}>
			<button
				style={styles.button}
				onClick={() => props.onClick(props.id)}
			>
				<img style={styles.image} src={props.source} alt="icon" />
			</button>
		</div>
	);
}

const styles = {
	button: {
		flex: 1,
		backgroundColor: colors.primary,
		borderRadius: constants.buttonRadius,
		padding: "5%",
		display: "flex",
	},
	image: {
		width: "100%",
		height: "100%",
		objectFit: "contain",
	},
};