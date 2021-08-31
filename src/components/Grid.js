import React, {useState, useEffect} from 'react';

import Row from "./Row";

export default function Grid(props) {
	const [iconButtons, setIconButtons] = useState([]);
	
	useEffect(() => {
		const iB = iconButtons.slice(0, props.numOfRows);
		for (let i=0; i<props.numOfRows; i++) {
			if (!iB[i]) {
				iB[i] = [];
			} else {
				iB[i] = iB[i].slice(0, props.numOfCols);
			}
			for (let j=iB[i].length; j<props.numOfCols; j++) {
				iB[i][j] = "../assets/favicon.png";
			}
		};
		setIconButtons(iB);
	}, [props.numOfRows, props.numOfCols]);
	
	const buttonDim = Math.min(
		window.innerHeight/(props.numOfRows+1),
		(window.innerWidth/2)/(props.numOfCols+1)
	);
	
	return (
		<div style={styles.container}>
			{iconButtons.map((row, i) => {
				return(
					<Row key={i} id={i} numOfCols={props.numOfCols} row={row} size={buttonDim}/>
				)
			})}
		</div>
	);
}

const styles = {
	container: {
		flex: 1,
		display: "flex",
		flexDirection: "column",
		justifyContent: "space-evenly",
	},
};