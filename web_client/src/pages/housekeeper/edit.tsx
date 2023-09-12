import {
  Edit,
  Box,
  TextField,
  FormControl,
  FormLabel,
  MenuItem,
  Select,
} from "@pankod/refine-mui";
import { useForm } from "@pankod/refine-react-hook-form";

import * as Yup from "yup";
import { yupResolver } from "@hookform/resolvers/yup";
import { REST_PUBLIC_URI } from "environment";
import { AxiosInstance } from "axios";
import { axiosInstance } from "@pankod/refine-simple-rest";
import { useState } from "react";

const schema = Yup.object({
  firstName: Yup.string().required("This field is required"),
  lastName: Yup.string().required("This field is required"),
  phone: Yup.string().required("This field is required"),
});

interface formDataType {
  firstName: string;
  lastName: string;
  phone: string;
}



export const HousekeeperEdit = () => {

  const {
    saveButtonProps,
    register,
    setValue,
    formState: { errors },
  } = useForm<formDataType>({ resolver: yupResolver(schema) });

  return (
    <Edit canDelete={false} saveButtonProps={saveButtonProps}>
      <Box
        component="form"
        sx={{ display: "flex", flexDirection: "column" }}
        autoComplete="off"
      >
        <TextField
          {...register("id")}
          required
          error={!!(errors as any)?.name}
          helperText={(errors as any)?.name?.message}
          margin="normal"
          fullWidth
          InputLabelProps={{ shrink: true }}
          type="text"
          label="Housekeeper Id"
          name="id"
          disabled
        />
        <TextField
          {...register("firstName", {
            required: "This field is required",
          })}
          required
          error={!!(errors as any)?.name}
          helperText={(errors as any)?.name?.message}
          margin="normal"
          fullWidth
          InputLabelProps={{ shrink: true }}
          type="text"
          label="First Name"
          name="firstName"
        />

        <TextField
          {...register("lastName")}
          error={!!(errors as any)?.backtest_end_at}
          helperText={(errors as any)?.backtest_end_at?.message}
          margin="normal"
          fullWidth
          InputLabelProps={{ shrink: true }}
          type="text"
          label="Last Name"
          name="lastName"
        />

        <TextField
          {...register("phone")}
          error={!!(errors as any)?.backtest_end_at}
          helperText={(errors as any)?.backtest_end_at?.message}
          margin="normal"
          fullWidth
          InputLabelProps={{ shrink: true }}
          type="text"
          label="phone"
          name="phone"
        />
      </Box>
    </Edit>
  );
};
