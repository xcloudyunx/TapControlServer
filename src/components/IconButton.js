import React from 'react';

import colors from "../config/colors";

export default function IconButton(props) {
	const handlePress = () => {
		console.log("pressed ", props.id);
	}
	
	return (
		<div style={{
			width: props.size,
			height: props.size,
			display: "flex",
		}}>
			<button
				style={Object.assign(
					{},
					styles.button,
					{
						width: props.size,
						height: props.size,
					}
				)}
				onClick={handlePress}
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
		borderRadius: "20%",
		padding: "5%",
		display: "flex",
	},
	image: {
		width: "100%",
		height: "100%",
		objectFit: "contain",
	},
};