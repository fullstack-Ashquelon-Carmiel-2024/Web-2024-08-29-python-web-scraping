import { createContext, useReducer } from "react";
import userReducer from "./userReducer";

const INITIAL_STATE = {
    user: {role: 'guest'}, tokenFamily: 0, sportBtn: 'secondary'
}

export const userContext = createContext(INITIAL_STATE);

export const UserContextProvider = ({children}) => {

    const [state,dispatchUser] = useReducer(userReducer,INITIAL_STATE);

    return (
        <userContext.Provider value={{user:state.user,sportBtn:state.sportBtn
                                                          ,dispatchUser}}>
            {children}
        </userContext.Provider>
    )
    
}